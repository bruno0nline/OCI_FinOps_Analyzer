# 📊 OCI FinOps Analyzer – CPU, Memória & Burstable Baseline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
![OCI](https://img.shields.io/badge/Cloud-Oracle_Cloud_Infrastructure-orange)
![FinOps](https://img.shields.io/badge/Focus-FinOps-blueviolet)
![Reports](https://img.shields.io/badge/Reports-CSV%20%7C%20XLSX%20%7C%20DOCX-success)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Ferramenta **open-source**, simples e poderosa, para analisar o uso de **CPU**, **Memória** e **baseline expansível (burstable)**
das instâncias OCI Compute e gerar recomendações automáticas de **FinOps** – incluindo **estimativa de economia/aumento de custo em real (BRL)**.

Desenvolvido e mantido por **Bruno Mendes Augusto**.

---

## ✨ Funcionalidades

- 🔍 Varredura automática de **todas as regiões** da tenancy.
- 🗂 Suporte a **todos os compartments** (raiz + filhos).
- ⏱ Análise histórica dos últimos **N dias** (padrão: 30).
- 📈 Cálculo de:
  - Média de CPU / Memória
  - Percentil 95 (P95) de CPU / Memória
- 🤖 Recomendações automáticas FinOps:
  - 🟩 `KEEP`
  - 🟥 `DOWNSIZE`, `DOWNSIZE-STRONG`, `DOWNSIZE-MEM`
  - 🟨 `UPSCALE`
  - 🔁 Sugestão de conversão para instância **burstable 12,5% ou 50%** quando fizer sentido
- 📤 Geração automática de:
  - Arquivo **CSV** detalhado
  - Planilha **Excel (.xlsx)** com cores por recomendação (verde, amarelo, vermelho)
  - **Relatório executivo em Word (.docx)** com:
    - Lista de recomendações
    - Estimativa de economia/aumento **em BRL por mês**
    - Resumo financeiro consolidado (downsize, upscale, burstable, economia líquida)

> ⚠️ As estimativas financeiras são calculadas em **real (BRL)** usando uma matriz simplificada de preços por família de forma (E3/E4/E5/E6/A1/A2/X9),
baseada na tabela pública da Oracle. Para clientes com contratos específicos, basta ajustar o dicionário `PRICE_MATRIX`
no script `oci_metrics_cpu_mem_word_report.py`.

---

## 📁 Estrutura do Projeto

```text
oci-metrics-cpu-mem-report/
├── src/
│   ├── oci_metrics_cpu_mem_media_ndays.py   # Script principal FinOps (CSV/XLSX)
│   ├── oci_metrics_cpu_mem_realtime.py      # Relatório rápido (30 min)
│   └── oci_metrics_cpu_mem_word_report.py   # Gera relatório executivo DOCX com valores em BRL
├── docs/
│   ├── README_WIKI.md                       # Guia interno para Wiki corporativa
│   └── PRESENTACAO_GESTAO.md                # Estrutura de apresentação para gestão
├── examples/
│   ├── sample_output.csv
│   └── sample_output.xlsx
├── requirements.txt
└── README.md
```

---

## 🚀 Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/bruno0nline/oci-metrics-cpu-mem-report.git
cd oci-metrics-cpu-mem-report
```

### 2. Criar e ativar ambiente virtual (Cloud Shell OCI)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Definir período de análise (em dias)

Exemplo: 30 dias

```bash
export METRICS_DAYS=30
```

### 4. Executar o relatório principal FinOps (CSV + XLSX)

```bash
python3 src/oci_metrics_cpu_mem_media_ndays.py
```

Saídas geradas na **home do usuário**:

```text
~/Relatorio_CPU_Memoria_media_30d_multi_region.csv
~/Relatorio_CPU_Memoria_media_30d_multi_region.xlsx
```

### 5. (Opcional) Relatório executivo em Word com estimativa em BRL

```bash
python3 src/oci_metrics_cpu_mem_word_report.py
```

Saída:

```text
~/Relatorio_FinOps_CPU_Mem_30d_multi_region.docx
```

Esse DOCX já vem pronto para ser anexado em e-mails ou usado em apresentações,
com um **resumo financeiro consolidado**:

- Total estimado de economia com **downsizing**
- Total estimado de aumento com **upscale**
- Total estimado de economia com **instâncias burstable**
- Economia líquida potencial (em BRL/mês)

---

## 📊 Exemplo de Recomendações

| Instância | CPU Mean | Mem Mean | Burstable | Recomendação    |
|----------|----------|----------|-----------|-----------------|
| vm-app01 |  9%      | 22%      | NO        | 🟥 DOWNSIZE      |
| vm-db02  | 65%      | 88%      | NO        | 🟨 UPSCALE       |
| vm-web03 | 43%      | 31%      | NO        | 🟩 KEEP          |
| vm-scan  |  4%      | 18%      | NO        | 🔁 BURSTABLE-12.5 |

---

## 🔧 Scripts disponíveis

- `oci_metrics_cpu_mem_media_ndays.py`  
  Analisa N dias de histórico, gera CSV/XLSX multi-região, calcula médias e P95, identifica baseline burstable e gera recomendação FinOps.

- `oci_metrics_cpu_mem_realtime.py`  
  Consulta rápida das métricas dos últimos 30 minutos para instâncias em execução.

- `oci_metrics_cpu_mem_word_report.py`  
  Lê o CSV consolidado, calcula **estimativas em BRL** com base na família de forma (E3/E4/E5/E6/A1/A2/X9) e gera um DOCX
  com recomendações detalhadas e **resumo financeiro consolidado**.

---

## 🤝 Contribuindo

Pull Requests são bem-vindos!  
Sugestões podem ser enviadas na aba **Issues** do repositório.

---

## 📜 Licença

Distribuído sob a licença **MIT**. Você pode usar este código em ambientes pessoais ou corporativos.
