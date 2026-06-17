# 🚀 Guia de Início Rápido

**Comece a otimizar seus custos OCI em 5 minutos!**


## ⚡ Início Rápido (Cloud Shell OCI)

```bash
# 1. Clone o repositório
git clone https://github.com/bruno0nline/oci-finops-analyzer.git
cd oci-finops-analyzer

# 2. Configure o ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Execute a análise
export METRICS_DAYS=30
python3 src/oci_metrics_cpu_mem_media_ndays.py

# 4. Gere o relatório executivo
python3 src/oci_metrics_cpu_mem_word_report.py
```

**Pronto!** Seus relatórios estão em `~/`


## 📊 Seus Relatórios

Após a execução, você terá:

```
~/Relatorio_CPU_Memoria_media_30d_multi_region.csv   # Dados detalhados
~/Relatorio_CPU_Memoria_media_30d_multi_region.xlsx  # Planilha colorida
~/Relatorio_FinOps_CPU_Mem_30d_multi_region.docx     # Relatório executivo
```


## 🎯 Próximos Passos

### 1. Revise o Relatório Excel

Abra o arquivo `.xlsx` e procure por:

### 2. Priorize Ações

**Alta Prioridade:**

**Média Prioridade:**

**Baixa Prioridade:**

### 3. Implemente Mudanças

```bash
# Exemplo: Redimensionar instância
oci compute instance update \
  --instance-id <instance-ocid> \
  --shape <new-shape>
```

### 4. Monitore Resultados

Aguarde 7 dias e execute novamente:

```bash
export METRICS_DAYS=7
python3 src/oci_metrics_cpu_mem_media_ndays.py
```


## 📖 Documentação Completa



## 🆘 Precisa de Ajuda?

### Problemas Comuns

**Erro de autenticação?**
```bash
oci setup config
```

**Módulo não encontrado?**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Sem dados?**

### Suporte



## 🎓 Aprenda Mais

### Entendendo as Recomendações

| Recomendação | CPU | Memória | Ação |
|--------------|-----|---------|------|
| KEEP | 30-70% | 40-80% | ✅ Nada |
| DOWNSIZE | <30% | <40% | 📉 Reduzir |
| DOWNSIZE-STRONG | <15% | <30% | 📉📉 Reduzir muito |
| UPSCALE | >70% | >80% | 📈 Aumentar |
| BURSTABLE | <10% | - | 🔄 Converter |

### Calculando Economia

```
Economia Mensal = (Shape Atual - Shape Recomendado) × 730h × Preço/hora
```

Exemplo:
```
VM.Standard.E4.Flex (4 OCPUs) → VM.Standard.E4.Flex (2 OCPUs)
Economia = (4 - 2) × 730 × R$ 0,06 = R$ 87,60/mês
```


## 🎯 Metas Recomendadas

### Primeira Análise

### Primeiro Mês

### Segundo Mês

### Terceiro Mês


## 💡 Dica Pro

**Automatize análises mensais:**

```bash
# Adicione ao crontab
crontab -e

# Execute todo dia 1º às 2h
0 2 1 * * cd ~/oci-finops-analyzer && source .venv/bin/activate && export METRICS_DAYS=30 && python3 src/oci_metrics_cpu_mem_media_ndays.py && python3 src/oci_metrics_cpu_mem_word_report.py
```


## 🌟 Casos de Sucesso

### Empresa A

### Empresa B


**Pronto para começar? Execute o primeiro comando e comece a economizar! 🚀**

```bash
git clone https://github.com/bruno0nline/oci-finops-analyzer.git && cd oci-finops-analyzer
```
