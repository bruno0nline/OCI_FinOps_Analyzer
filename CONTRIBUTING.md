# Contribuindo para OCI FinOps Analyzer

Obrigado por considerar contribuir com o OCI FinOps Analyzer! 🎉

## 🤝 Como Contribuir

### 1. Fork e Clone

```bash
git clone https://github.com/seu-usuario/oci-finops-analyzer.git
cd oci-finops-analyzer
```

### 2. Crie um Ambiente Virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Crie uma Branch

```bash
git checkout -b feature/minha-feature
# ou
git checkout -b fix/meu-bugfix
```

### 4. Faça suas Alterações

- Mantenha o código limpo e bem documentado
- Siga as convenções de código Python (PEP 8)
- Adicione docstrings para funções e classes
- Teste suas alterações

### 5. Commit

Use mensagens de commit descritivas seguindo o padrão:

```bash
git add .
git commit -m "feat: adiciona suporte para análise de Block Volumes"
```

### 6. Push e Pull Request

```bash
git push origin feature/minha-feature
```

Abra um Pull Request descrevendo:
- O que foi alterado
- Por que foi alterado
- Como testar

---

## 📝 Padrões de Commit

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação (sem mudança de código)
- `refactor:` Refatoração de código
- `test:` Adição ou correção de testes
- `chore:` Tarefas de manutenção

**Exemplos:**
```
feat: adiciona análise de custos de Block Volumes
fix: corrige cálculo de percentil 95
docs: atualiza guia de instalação
refactor: melhora performance da coleta de métricas
```

---

## 🎯 Áreas para Contribuição

### Funcionalidades Desejadas

- [ ] Suporte para análise de Block Volumes
- [ ] Suporte para análise de Load Balancers
- [ ] Dashboard web interativo
- [ ] Integração com Slack/Teams para notificações
- [ ] Análise de custos de rede
- [ ] Suporte para múltiplas tenancies
- [ ] API REST para integração
- [ ] Testes automatizados

### Melhorias de Código

- [ ] Adicionar testes unitários
- [ ] Melhorar tratamento de erros
- [ ] Adicionar logging estruturado
- [ ] Otimizar performance de coleta
- [ ] Adicionar cache de métricas

### Documentação

- [ ] Tutoriais em vídeo
- [ ] Exemplos de uso avançado
- [ ] Guia de troubleshooting
- [ ] Documentação de API
- [ ] Tradução para inglês

---

## 🧪 Testes

Antes de submeter um PR, certifique-se de:

1. Testar o código em ambiente OCI real
2. Verificar se não há erros de sintaxe
3. Validar a saída dos relatórios
4. Testar com diferentes configurações de tenancy

```bash
# Executar testes (quando disponíveis)
python -m pytest tests/

# Verificar estilo de código
flake8 src/
black --check src/
```

---

## 📋 Checklist do Pull Request

Antes de submeter, verifique:

- [ ] O código segue o padrão PEP 8
- [ ] Adicionei docstrings para novas funções
- [ ] Atualizei o README se necessário
- [ ] Testei as alterações em ambiente real
- [ ] O commit segue o padrão Conventional Commits
- [ ] Não há credenciais ou dados sensíveis no código

---

## 🐛 Reportando Bugs

Ao reportar um bug, inclua:

1. **Descrição clara** do problema
2. **Passos para reproduzir**
3. **Comportamento esperado** vs **comportamento atual**
4. **Ambiente:**
   - Versão do Python
   - Versão do OCI SDK
   - Sistema operacional
   - Região OCI
5. **Logs de erro** (se aplicável)

---

## 💡 Sugerindo Funcionalidades

Ao sugerir uma funcionalidade:

1. **Descreva o problema** que ela resolve
2. **Explique a solução proposta**
3. **Forneça exemplos** de uso
4. **Considere alternativas**

---

## 🔒 Segurança

Se você encontrar uma vulnerabilidade de segurança:

- **NÃO** abra uma issue pública
- Envie um email para: brunomendesaugusto@gmail.com
- Descreva a vulnerabilidade em detalhes
- Aguarde resposta antes de divulgar

---

## 📜 Código de Conduta

### Nosso Compromisso

Estamos comprometidos em proporcionar uma experiência acolhedora e livre de assédio para todos.

### Comportamento Esperado

- Use linguagem acolhedora e inclusiva
- Respeite pontos de vista diferentes
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade

### Comportamento Inaceitável

- Linguagem ou imagens sexualizadas
- Comentários insultuosos ou depreciativos
- Assédio público ou privado
- Publicação de informações privadas de terceiros

---

## 🙏 Agradecimentos

Obrigado por contribuir para tornar o OCI FinOps Analyzer melhor!

Sua contribuição ajuda a comunidade FinOps a otimizar custos e melhorar a eficiência na nuvem.

---

## 📞 Dúvidas?

- Abra uma [Discussion](https://github.com/bruno0nline/oci-finops-analyzer/discussions)
- Entre em contato: brunomendesaugusto@gmail.com

---

**Happy Coding! 🚀**
