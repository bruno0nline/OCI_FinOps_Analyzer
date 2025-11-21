# 📊 OCI FinOps Analyzer — CPU, Memory & Burstable Baseline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
![OCI](https://img.shields.io/badge/Cloud-Oracle_Cloud_Infrastructure-orange)
![FinOps](https://img.shields.io/badge/Focus-FinOps-blueviolet)
![Reports](https://img.shields.io/badge/Reports-CSV%20%26%20XLSX%20%26%20DOCX-success)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Ferramenta **open-source**, simples e poderosa, para analisar o uso de **CPU**, **Memória** e a **baseline expansível (burstable)** das
instâncias OCI Compute e gerar recomendações automáticas de **FinOps** – incluindo **estimativa de economia/aumento de custo**.

Desenvolvido e mantido por **Bruno Mendes Augusto**.

---

## ✨ Funcionalidades

- 🔍 Varredura automática de **todas as regiões** da tenancy
- 🗂 Suporte a **todos os compartments** (raiz + filhos)
- ⏱ Análise histórica dos últimos **N dias** (padrão: 30)
- 📈 Cálculo de:
  - Média de CPU / Memória
  - Percentil 95 (P95) de CPU / Memória
- 🤖 Recomendações automáticas FinOps:
  - 🟩 `KEEP`
  - 🟥 `DOWNSIZE`, `DOWNSIZE-STRONG`, `DOWNSIZE-MEM`
  - 🟨 `UPSCALE`
- 💡 Detecção de **instâncias expansíveis (burstable)**:
  - Identifica se a forma está com baseline 12,5%, 50% ou 100%
  - Sugere conversão para burstable quando fizer sentido (12,5% ou 50%)
- 📤 Geração automática de:
  - Arquivo **CSV** detalhado
  - Planilha **Excel (.xlsx)** com cores por recomendação (verde, amarelo, vermelho)
  - Relatório **Word (.docx)** com texto explicativo e **estimativa consolidada de economia/impacto**

Compatível com **OCI Cloud Shell** e também com qualquer ambiente com Python + OCI SDK configurados.

---

## 📁 Estrutura do Projeto

```text
oci-metrics-cpu-mem-report/
├── src/
│   ├── oci_metrics_cpu_mem_media_ndays.py   # Script principal FinOps (CSV + XLSX)
│   ├── oci_metrics_cpu_mem_realtime.py      # Relatório rápido (30 min, console)
│   └── oci_metrics_cpu_mem_word_report.py   # Gera relatório executivo em Word
├── docs/
│   ├── README_WIKI.md                       # Documentação para wiki interna
│   └── PRESENTACAO_GESTAO.md                # Visão executiva para gestão
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

### 2. Criar e ativar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
# no Windows:
# .venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Definir período de análise (em dias)

Exemplo: 30 dias

```bash
export METRICS_DAYS=30
# no Windows (PowerShell):
# $env:METRICS_DAYS=30
```

### 5. Executar o relatório principal FinOps (CSV + XLSX)

```bash
python3 src/oci_metrics_cpu_mem_media_ndays.py
```

Saídas geradas na **home do usuário**:

```text
~/Relatorio_CPU_Memoria_media_30d_multi_region.csv
~/Relatorio_CPU_Memoria_media_30d_multi_region.xlsx
```

### 6. Gerar relatório executivo em Word (com estimativas de custo)

Depois de gerar o CSV do passo anterior:

```bash
python3 src/oci_metrics_cpu_mem_word_report.py
```

Saída:

```text
~/Relatorio_FinOps_CPU_Mem_30d_multi_region.docx
```

---

## 📊 Exemplo de Recomendações (tabela Excel)

| Instância | CPU Mean | Mem Mean | Burstable | Recomendação   |
|----------|----------|----------|-----------|----------------|
| vm-app01 | 9%       | 22%      | 100%      | 🟥 DOWNSIZE    |
| vm-db02  | 65%      | 88%      | 100%      | 🟨 UPSCALE     |
| vm-web03 | 34%      | 41%      | 12,5%     | 🟩 KEEP        |
| vm-scan  | 13%      | 18%      | OFF       | 💡 BURSTABLE-12.5 |

---

## 🔧 Scripts disponíveis

- `oci_metrics_cpu_mem_media_ndays.py`  
  Analisa N dias de histórico em todas as regiões/compartments, calcula médias e P95 de CPU/Memória, identifica baseline
  burstable e gera relatórios **CSV/XLSX** com recomendação FinOps.

- `oci_metrics_cpu_mem_realtime.py`  
  Consulta rápida das métricas de CPU/Memória dos últimos 30 minutos para instâncias em execução, direto no console.

- `oci_metrics_cpu_mem_word_report.py`  
  Lê o CSV gerado pelo script principal e cria um **relatório em Word** com:
  - Seções separadas para **downsize**, **upscale** e **instâncias expansíveis**
  - Sugestão de nova configuração (OCPUs/memória ou baseline)
  - **Estimativa de economia ou impacto mensal por instância**
  - **Resumo consolidado** com:
    - Total estimado de economia por downsize
    - Total estimado de aumento por upscale
    - Total estimado de economia por conversão para burstable
    - Economia líquida potencial

> ⚠️ Os valores de custo são **estimativas simples em USD** com base em preços de tabela genéricos.
> Ajuste as constantes `OCPU_PRICE_HOUR`, `MEM_GB_PRICE_HOUR` e `HOURS_MONTH` no script `oci_metrics_cpu_mem_word_report.py`
> para refletir a realidade contratual do seu cliente.

---

## 🤝 Contribuindo

Pull Requests são bem-vindos!  
Sugestões podem ser enviadas na aba **Issues** do repositório.

Se este projeto te ajudou em algum ambiente real (cliente ou interno), considere deixar uma ⭐ no GitHub. 🙂

---

## 📜 Licença

Distribuído sob a licença **MIT**. Você pode usar este código em ambientes pessoais ou corporativos.

Autor original: **Bruno Mendes Augusto**.
