# 🔧 Instruções de Instalação e Configuração - CrewAI System

## 📋 Pré-requisitos

- ✅ Python 3.12+
- ✅ UV (gerenciador de dependências)
- ✅ Google Gemini API Key
- ✅ Sistema operacional: macOS, Linux ou Windows

## 🚀 Instalação Rápida

### 1. Verificar Dependências
```bash
# Verificar Python
python --version  # Deve ser 3.12+

# Verificar UV
uv --version
```

### 2. Configurar API Key do Gemini
```bash
# Obter API Key em: https://aistudio.google.com/app/apikey
export GEMINI_API_KEY="sua_api_key_aqui"

# Para tornar permanente (adicione ao ~/.zshrc ou ~/.bashrc)
echo 'export GEMINI_API_KEY="sua_api_key_aqui"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Instalar Dependências
```bash
# Na pasta principal do projeto
cd /caminho/para/agenteinstagram-novas_implementa-oes
uv sync
```

## ⚡ Execução Rápida

### Opção 1: Script Automático (Recomendado)
```bash
cd crewai_system/scripts
./quick_start.sh
```

### Opção 2: Manual
```bash
cd crewai_system/scripts

# Verificar saúde
uv run crew_health_check.py

# Executar análise
uv run crew_gemini_simples.py
```

## 📁 Localização dos Arquivos

### Scripts Principais
- `scripts/crew_gemini_simples.py` - **PRINCIPAL - Use este!**
- `scripts/crew_health_check.py` - Verificação de saúde
- `scripts/quick_start.sh` - Script de execução rápida

### Configurações
- `config/crew_config.yaml` - Configuração dos 6 agentes
- `config/crew.yaml` - Configuração original

### Documentação
- `docs/README_CREW.md` - Guia completo (45 páginas)
- `README.md` - Guia principal desta pasta

### Relatórios
- `reports/` - Pasta onde os relatórios são salvos automaticamente

## 🔍 Verificação da Instalação

### Teste Rápido
```bash
cd crewai_system/scripts
uv run crew_health_check.py
```

**Resultado esperado:**
```
✅ Sistema CrewAI - Health Check
✅ Gemini API Key configurada
✅ Dependências instaladas
✅ Arquivos necessários encontrados
🎉 Sistema 100% operacional!
```

## 🛠️ Configuração Avançada

### Personalizar Agentes
Edite `config/crew_config.yaml`:
```yaml
agents:
  arquiteto_software:
    role: "Arquiteto de Software Sênior"
    goal: "Suas metas personalizadas aqui"
    # ... outras configurações
```

### Personalizar Template de Relatório
Edite `templates/template_relatorio_final.md` para customizar o formato.

### Configurar Thresholds
No `crew_config.yaml`, ajuste os limites:
```yaml
quality_thresholds:
  security_issues: 5
  code_coverage: 60
  # ... outros thresholds
```

## 📊 Monitoramento de Custos

### Custos Típicos (Gemini 2.5 Flash)
- **Por análise completa:** $0.15 - $0.25 USD
- **Por mês (10 análises):** ~$2.50 USD
- **Muito econômico** comparado a GPT-4

### Como Monitorar
1. Acesse: https://aistudio.google.com/app/billing
2. Monitore usage diário/mensal
3. Configure alertas de billing

## 🆘 Resolução de Problemas

### ❌ "GEMINI_API_KEY não configurada"
```bash
# Solução 1: Configurar temporariamente
export GEMINI_API_KEY="sua_key"

# Solução 2: Configurar permanentemente
echo 'export GEMINI_API_KEY="sua_key"' >> ~/.zshrc
source ~/.zshrc
```

### ❌ "Módulo não encontrado"
```bash
# Na pasta principal do projeto (não na crewai_system)
cd ..
uv sync
```

### ❌ "Permission denied" no quick_start.sh
```bash
chmod +x crewai_system/scripts/quick_start.sh
```

### ❌ "Timeout" durante análise
- ⏳ **Normal:** Primeira execução pode demorar mais
- 🔄 **Solução:** Execute novamente - o sistema tem retry automático
- 🌐 **Rede:** Verifique conexão com internet

### ❌ Relatório incompleto
- 🔄 Execute novamente
- 📊 Sistema salva progresso parcial
- ✅ Relatório será recuperado automaticamente

## 📈 Otimização de Performance

### Para Análises Mais Rápidas
1. **Use SSD** para melhor I/O
2. **Boa conexão** de internet
3. **Minimize outros processos** durante análise

### Para Reduzir Custos
1. **Configure thresholds** mais altos no YAML
2. **Reutilize relatórios** recentes
3. **Execute batch** de análises juntas

## 🔐 Segurança

### Proteção da API Key
```bash
# ❌ NUNCA faça isso (exposto no código):
GEMINI_API_KEY = "sk-proj-abc123..."

# ✅ SEMPRE use variáveis de ambiente:
export GEMINI_API_KEY="sua_key"
```

### Backup de Configurações
```bash
# Backup das configurações
cp config/crew_config.yaml config/crew_config.yaml.backup

# Backup dos relatórios
tar -czf reports_backup.tar.gz reports/
```

## 🎯 Próximos Passos

Após a instalação:

1. ✅ **Execute primeira análise** com `quick_start.sh`
2. ✅ **Revise o relatório** gerado em `reports/`
3. ✅ **Personalize configurações** em `config/`
4. ✅ **Consulte documentação** completa em `docs/`

## 📞 Suporte

### Documentação
- `README.md` - Guia principal
- `docs/README_CREW.md` - Documentação completa

### Logs
- Os logs são exibidos no terminal durante execução
- Relatórios incluem detalhes técnicos completos

---

**💡 Dica:** Comece sempre com o `quick_start.sh` para uma experiência sem complicações!
