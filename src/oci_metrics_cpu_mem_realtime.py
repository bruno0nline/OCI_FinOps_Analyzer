
import os
from datetime import datetime, timedelta, timezone

import oci
from oci.monitoring.models import SummarizeMetricsDataDetails

cfg = oci.config.from_file()
tenancy_id = cfg["tenancy"]


def get_all_regions(identity_client):
    resp = identity_client.list_region_subscriptions(tenancy_id)
    return [r.region_name for r in resp.data]


def get_all_compartments(identity_client):
    result = oci.pagination.list_call_get_all_results(
        identity_client.list_compartments,
        tenancy_id,
        compartment_id_in_subtree=True
    )
    return [c for c in result.data if c.lifecycle_state == "ACTIVE"]


def main():
    identity = oci.identity.IdentityClient(cfg)
    regions = get_all_regions(identity)
    compartments = get_all_compartments(identity)

    start = datetime.now(timezone.utc) - timedelta(minutes=30)
    end = datetime.now(timezone.utc)

    print("Consulta rápida (30 min) de CPU/Memória para instâncias RUNNING.\n")

    for region in regions:
        print(f"===== Região: {region} =====")
        region_cfg = dict(cfg)
        region_cfg["region"] = region

        compute = oci.core.ComputeClient(region_cfg)
        monitoring = oci.monitoring.MonitoringClient(region_cfg)

        for comp in compartments:
            comp_id = comp.id
            comp_name = comp.name

            instances = oci.pagination.list_call_get_all_results(
                compute.list_instances,
                compartment_id=comp_id
            ).data

            running = [i for i in instances if i.lifecycle_state == "RUNNING"]
            if not running:
                continue

            print(f"  Compartment: {comp_name}")

            for inst in running:
                print(f"  -> {inst.display_name}")

                def get_metric(metric_name):
                    query = f'{metric_name}[5m]{{resourceId = "{inst.id}"}}.mean()'
                    details = SummarizeMetricsDataDetails(
                        namespace="oci_computeagent",
                        query=query,
                        start_time=start,
                        end_time=end,
                    )
                    resp = monitoring.summarize_metrics_data(
                        compartment_id=comp_id,
                        summarize_metrics_data_details=details,
                    )
                    if not resp.data or not resp.data[0].aggregated_datapoints:
                        return None
                    return resp.data[0].aggregated_datapoints[-1].value

                cpu = get_metric("CpuUtilization")
                mem = get_metric("MemoryUtilization")

                print(f"     CPU={cpu if cpu is not None else 'sem dado'} % | MEM={mem if mem is not None else 'sem dado'} %")

    print("\nFim da consulta.")

if __name__ == "__main__":
    main()
