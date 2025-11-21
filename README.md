# 📊 OCI FinOps Analyzer — CPU, Memory & Burstable Baseline

Ferramenta para analisar uso de **CPU / Memória** das instâncias OCI Compute,
identificar oportunidades de **FinOps** e gerar:

- CSV consolidado multi-região
- Planilha Excel com cores (KEEP / DOWNSIZE / UPSCALE)
- Relatório Word com recomendações e **estimativa de custo mensal** (economia ou aumento)

Desenvolvido por **Bruno Mendes Augusto**.

## 🚀 Uso rápido

```bash
git clone https://github.com/bruno0nline/oci-metrics-cpu-mem-report.git
cd oci-metrics-cpu-mem-report

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export METRICS_DAYS=30
python3 src/oci_metrics_cpu_mem_media_ndays.py
python3 src/oci_metrics_cpu_mem_word_report.py
```

Arquivos gerados na home do usuário:

- `Relatorio_CPU_Memoria_media_30d_multi_region.csv`
- `Relatorio_CPU_Memoria_media_30d_multi_region.xlsx`
- `Relatorio_FinOps_CPU_Mem_30d_multi_region.docx`

## 💰 Parâmetros de custo (estimativa)

Os scripts usam valores padrão aproximados, baseados na lista pública de preços da OCI.
Para cada cliente/região você **deve ajustar** via variáveis de ambiente:

```bash
export OCI_COST_CURRENCY=BRL
export OCI_COST_OCPU_HOUR=0.70      # exemplo
export OCI_COST_MEM_GB_HOUR=0.03    # exemplo
```

Esses valores são usados para estimar:

- Custo atual mensal da instância
- Custo estimado após downsize/upscale
- Economia / aumento de custo estimado por instância

As estimativas aparecem automaticamente no relatório Word.
