# Instalação e Configuração

## 📋 Pré-requisitos

### Software Necessário

- **Python 3.9 ou superior**
- **OCI CLI** configurado
- **Git**

### Permissões OCI Necessárias

Para executar o OCI FinOps Analyzer, você precisa das seguintes permissões:

```
Allow group FinOpsAnalyzers to read instances in tenancy
Allow group FinOpsAnalyzers to read metrics in tenancy
Allow group FinOpsAnalyzers to read compartments in tenancy
```

---

## 🚀 Instalação

### Opção 1: Cloud Shell OCI (Recomendado)

O Cloud Shell já vem com Python e OCI CLI configurados:

```bash
# 1. Clonar repositório
git clone https://github.com/bruno0nline/oci-finops-analyzer.git
cd oci-finops-analyzer

# 2. Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar
export METRICS_DAYS=30
python3 src/oci_metrics_cpu_mem_media_ndays.py
```

### Opção 2: Instalação Local

#### Linux/Mac

```bash
# 1. Instalar Python 3.9+
sudo apt update && sudo apt install python3 python3-pip python3-venv  # Ubuntu/Debian
# ou
brew install python@3.9  # macOS

# 2. Instalar OCI CLI
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

# 3. Configurar OCI CLI
oci setup config

# 4. Clonar e configurar projeto
git clone https://github.com/bruno0nline/oci-finops-analyzer.git
cd oci-finops-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Windows

```powershell
# 1. Instalar Python 3.9+ (baixar de python.org)

# 2. Instalar OCI CLI
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1'))"

# 3. Configurar OCI CLI
oci setup config

# 4. Clonar e configurar projeto
git clone https://github.com/bruno0nline/oci-finops-analyzer.git
cd oci-finops-analyzer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## ⚙️ Configuração

### 1. Configurar OCI CLI

Se ainda não configurou o OCI CLI:

```bash
oci setup config
```

Você precisará fornecer:
- **User OCID**
- **Tenancy OCID**
- **Region** (ex: sa-saopaulo-1)
- **API Key** (será gerada automaticamente)

### 2. Verificar Configuração

```bash
# Testar conectividade
oci iam region list

# Listar compartments
oci iam compartment list --all
```

### 3. Configurar Variáveis de Ambiente

```bash
# Período de análise (em dias)
export METRICS_DAYS=30

# Opcional: Configurar profile específico
export OCI_CLI_PROFILE=DEFAULT
```

---

## 🔧 Configuração Avançada

### Ajustar Limites de Recomendação

Edite `src/oci_metrics_cpu_mem_media_ndays.py`:

```python
# Limites para CPU
CPU_DOWNSIZE_THRESHOLD = 30      # CPU < 30% = DOWNSIZE
CPU_DOWNSIZE_STRONG = 15         # CPU < 15% = DOWNSIZE-STRONG
CPU_UPSCALE_THRESHOLD = 70       # CPU > 70% = UPSCALE

# Limites para Memória
MEM_DOWNSIZE_THRESHOLD = 40      # Mem < 40% = DOWNSIZE
MEM_UPSCALE_THRESHOLD = 80       # Mem > 80% = UPSCALE

# Limites para Burstable
BURSTABLE_12_5_THRESHOLD = 10    # CPU < 10% = BURSTABLE-12.5
BURSTABLE_50_THRESHOLD = 45      # CPU < 45% = BURSTABLE-50
```

### Ajustar Matriz de Preços

Edite `src/oci_metrics_cpu_mem_word_report.py`:

```python
PRICE_MATRIX = {
    'E3': 0.05,   # Preço por OCPU/hora em BRL
    'E4': 0.06,
    'E5': 0.07,
    'E6': 0.08,
    'A1': 0.04,
    'A2': 0.045,
    'X9': 0.09,
}
```

### Configurar Múltiplos Profiles

Para analisar múltiplas tenancies:

```bash
# Configurar profiles
oci setup config --profile tenancy1
oci setup config --profile tenancy2

# Executar para cada tenancy
export OCI_CLI_PROFILE=tenancy1
python3 src/oci_metrics_cpu_mem_media_ndays.py

export OCI_CLI_PROFILE=tenancy2
python3 src/oci_metrics_cpu_mem_media_ndays.py
```

---

## 🐛 Troubleshooting

### Erro: "Service error: NotAuthenticated"

**Solução:**
```bash
# Reconfigurar OCI CLI
oci setup config

# Verificar permissões do arquivo de configuração
chmod 600 ~/.oci/config
chmod 600 ~/.oci/oci_api_key.pem
```

### Erro: "ModuleNotFoundError: No module named 'oci'"

**Solução:**
```bash
# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Reinstalar dependências
pip install -r requirements.txt
```

### Erro: "No data found for instance"

**Possíveis causas:**
- Instância muito recente (< 1 hora)
- Métricas não habilitadas
- Permissões insuficientes

**Solução:**
```bash
# Verificar permissões
oci iam policy list --compartment-id <tenancy-ocid>

# Verificar se métricas estão disponíveis
oci monitoring metric list --compartment-id <compartment-ocid>
```

### Performance Lenta

**Otimizações:**

1. **Reduzir período de análise:**
```bash
export METRICS_DAYS=7  # Ao invés de 30
```

2. **Analisar compartments específicos:**
Edite o script para filtrar compartments

3. **Usar Cloud Shell:**
Execução mais rápida por estar na rede OCI

---

## 📊 Verificação da Instalação

Execute o teste de conectividade:

```bash
python3 src/oci_metrics_cpu_mem_realtime.py
```

Se tudo estiver configurado corretamente, você verá:
```
✅ Conectado à tenancy: <nome-da-tenancy>
✅ Regiões disponíveis: 3
✅ Compartments encontrados: 15
🔍 Coletando métricas...
```

---

## 📞 Suporte

Se você encontrar problemas:

1. Verifique a [documentação oficial do OCI CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)
2. Consulte as [Issues do GitHub](https://github.com/bruno0nline/oci-finops-analyzer/issues)
3. Abra uma nova issue com detalhes do erro

---

## 🔄 Atualização

Para atualizar para a versão mais recente:

```bash
cd oci-finops-analyzer
git pull origin main
pip install -r requirements.txt --upgrade
```

---

**Pronto! Agora você está pronto para começar a otimizar seus custos OCI! 🚀**
