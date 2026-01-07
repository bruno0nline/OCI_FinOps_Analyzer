import os
import time
import csv
from datetime import datetime, timedelta, timezone

import oci
from oci.monitoring.models import SummarizeMetricsDataDetails
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# =============================
# Configurações padrão
# =============================
DEFAULT_DAYS = 30
DAYS = int(os.getenv("METRICS_DAYS", DEFAULT_DAYS))

MAX_RETRIES = 3
RETRY_SLEEP = 3

homedir = os.path.expanduser("~")
CSV_PATH = os.path.join(homedir, f"Relatorio_CPU_Memoria_media_{DAYS}d_multi_region.csv")
XLSX_PATH = os.path.join(homedir, f"Relatorio_CPU_Memoria_media_{DAYS}d_multi_region.xlsx")

cfg = oci.config.from_file()
tenancy_id = cfg["tenancy"]

identity = oci.identity.IdentityClient(cfg)

# =============================
# Utilidades OCI
# =============================
def get_all_regions():
    return [r.region_name for r in identity.list_region_subscriptions(tenancy_id).data]

def get_all_compartments():
    result = oci.pagination.list_call_get_all_results(
        identity.list_compartments,
        tenancy_id,
        compartment_id_in_subtree=True
    )
    return [c for c in result.data if c.lifecycle_state == "ACTIVE"]

def summarize_with_retry(client, details):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return client.summarize_metrics_data(details).data
        except Exception as e:
            if "429" in str(e) and attempt < MAX_RETRIES:
                time.sleep(RETRY_SLEEP * attempt)
            else:
                raise

# =============================
# Lógica principal
# =============================
def main():
    start = datetime.now(timezone.utc) - timedelta(days=DAYS)
    end = datetime.now(timezone.utc)

    rows = []

    for region in get_all_regions():
        cfg_region = cfg.copy()
        cfg_region["region"] = region

        compute = oci.core.ComputeClient(cfg_region)
        monitoring = oci.monitoring.MonitoringClient(cfg_region)

        for comp in get_all_compartments():
            instances = compute.list_instances(comp.id).data

            for inst in instances:
                if inst.lifecycle_state != "RUNNING":
                    continue

                dimensions = {"resourceId": inst.id}

                cpu_details = SummarizeMetricsDataDetails(
                    namespace="oci_computeagent",
                    query="CpuUtilization[1m].mean()",
                    start_time=start,
                    end_time=end,
                    dimensions=dimensions
                )

                mem_details = SummarizeMetricsDataDetails(
                    namespace="oci_computeagent",
                    query="MemoryUtilization[1m].mean()",
                    start_time=start,
                    end_time=end,
                    dimensions=dimensions
                )

                try:
                    cpu_data = summarize_with_retry(monitoring, cpu_details)
                    mem_data = summarize_with_retry(monitoring, mem_details)

                    cpu_vals = [dp.value for item in cpu_data for dp in item.datapoints]
                    mem_vals = [dp.value for item in mem_data for dp in item.datapoints]

                    cpu_mean = sum(cpu_vals) / len(cpu_vals) if cpu_vals else None
                    mem_mean = sum(mem_vals) / len(mem_vals) if mem_vals else None

                except Exception:
                    cpu_mean = None
                    mem_mean = None

                rows.append({
                    "region": region,
                    "compartment": comp.name,
                    "instance_name": inst.display_name,
                    "instance_ocid": inst.id,
                    "shape": inst.shape,
                    "ocpus": inst.shape_config.ocpus if inst.shape_config else None,
                    "memory_gb": inst.shape_config.memory_in_gbs if inst.shape_config else None,
                    "cpu_mean_percent": round(cpu_mean, 2) if cpu_mean else "no-data",
                    "mem_mean_percent": round(mem_mean, 2) if mem_mean else "no-data",
                })

    # CSV
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    # XLSX
    wb = Workbook()
    ws = wb.active
    ws.append(list(rows[0].keys()))

    for r in rows:
        ws.append(list(r.values()))

    wb.save(XLSX_PATH)

    print(f"CSV gerado: {CSV_PATH}")
    print(f"XLSX gerado: {XLSX_PATH}")

if __name__ == "__main__":
    main()
