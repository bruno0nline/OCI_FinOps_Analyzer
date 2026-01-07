#!/bin/bash
set -e

echo "▶️ OCI FinOps Analyzer – Execução completa"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 src/oci_metrics_cpu_mem_media_ndays.py
python3 src/oci_metrics_cpu_mem_word_technical.py
python3 src/oci_metrics_cpu_mem_word_top5.py

echo "✅ Relatórios gerados com sucesso"
