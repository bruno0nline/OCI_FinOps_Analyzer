
import os
from datetime import datetime, timedelta, timezone

import oci
from oci.monitoring.models import SummarizeMetricsDataDetails

cfg = oci.config.from_file()
tenancy_id = cfg["tenancy"]
identity = oci.identity.IdentityClient(cfg)

region = cfg.get("region")
region_cfg = dict(cfg)
compute = oci.core.ComputeClient(region_cfg)
monitoring = oci.monitoring.MonitoringClient(region_cfg)

now = datetime.now(timezone.utc)
start = now - timedelta(minutes=30)
end = now

INTERVAL = "1m"


def get_metric_stats(inst_id, metric_name):
    query = f'{metric_name}[{INTERVAL}]{{resourceId = "{inst_id}"}}.mean()'
    details = SummarizeMetricsDataDetails(
        namespace="oci_computeagent",
        query=query,
        start_time=start,
        end_time=end,
    )
    resp = monitoring.summarize_metrics_data(
        compartment_id=tenancy_id,
        summarize_metrics_data_details=details,
    )
    if not resp.data or not resp.data[0].aggregated_datapoints:
        return None
    values = [dp.value for dp in resp.data[0].aggregated_datapoints if dp.value is not None]
    if not values:
        return None
    return sum(values) / len(values)


def main():
    print(f"Região atual: {region}")
    instances = oci.pagination.list_call_get_all_results(
        compute.list_instances,
        compartment_id=tenancy_id,
    ).data

    running = [i for i in instances if i.lifecycle_state == 'RUNNING']
    if not running:
        print("Nenhuma instância RUNNING encontrada.")
        return

    for inst in running:
        cpu = get_metric_stats(inst.id, "CpuUtilization")
        mem = get_metric_stats(inst.id, "MemoryUtilization")
        print(f"""Instância: {inst.display_name}
  CPU média (30min): {cpu if cpu is not None else 'no-data'}
  MEM média (30min): {mem if mem is not None else 'no-data'}
""")


if __name__ == "__main__":
    main()
