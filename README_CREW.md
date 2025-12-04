# 🚀 CrewAvaliadora - Sistema de Avaliação Ultra-Profissional | Ultra-Professional Assessment System

## 🇧🇷 Português

Sistema plug-and-play que utiliza **6 especialistas IA** para gerar análises profissionais de codebase usando **Gemini 2.5 Flash**.

## 🇺🇸 English

Plug-and-play system that uses **6 AI specialists** to generate professional codebase analysis using **Gemini 2.5 Flash**.

---

## 📋 Visão Geral | Overview

### 🎯 Fluxo Completo | Complete Flow

```
📂 Codebase → 🐍 Script Análise → 📄 Relatório → 🤝 CrewAI → 📑 Relatório Ultra-Profissional
📂 Codebase → 🐍 Analysis Script → 📄 Report → 🤝 CrewAI → 📑 Ultra-Professional Report
```

### 🎭 Especialistas da Crew | Crew Specialists

| 🇧🇷 Agente | 🇺🇸 Agent | 🎯 Foco | Focus |
|-----------|----------|---------|-------|
| 📐 **Arquiteto de Software** | **Software Architect** | Arquitetura & Design Patterns | Architecture & Design Patterns |
| 🧪 **Engenheiro de Qualidade** | **QA Engineer** | Testes & Qualidade | Testing & Quality |
| 📄 **Documentador Técnico** | **Technical Writer** | Documentação & Onboarding | Documentation & Onboarding |
| 🚀 **Product Manager** | **Product Manager** | Viabilidade Comercial | Business Viability |
| ⚖️ **Especialista Legal** | **Legal Specialist** | Compliance & Riscos | Compliance & Risks |
| 🤖 **Engenheiro de IA** | **AI Engineer** | Otimização de LLMs | LLM Optimization |

---

## 🚀 Quick Start

### 1. **Pré-requisitos | Prerequisites**

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Google Gemini API Key

### 2. **Setup**

```bash
# Clone
git clone <repo>
cd CrewAvaliadora

# Install
uv sync

# Configure
cp .env.example .env
# 🇧🇷 Adicione sua chave API
# 🇺🇸 Add your API key
```

### 3. **Executar | Run**

```bash
# 🇧🇷 Análise completa
# 🇺🇸 Complete analysis
uv run python src/main.py

# 🇧🇷 Interface Web
# 🇺🇸 Web Interface
uv run streamlit run src/streamlit_app.py
```

---

## 📁 Estrutura dos Arquivos | File Structure

```
CrewAvaliadora/
├── src/
│   ├── main.py                  # 🇧🇷 Entrypoint CLI | 🇺🇸 CLI Entrypoint
│   ├── streamlit_app.py         # 🇧🇷 Interface Web | 🇺🇸 Web Interface
│   ├── crew/                    # 🇧🇷 Lógica CrewAI | 🇺🇸 CrewAI Logic
│   └── config/                  # 🇧🇷 Configurações | 🇺🇸 Configuration
├── docs/                        # 🇧🇷 Documentação | 🇺🇸 Documentation
└── outputs/                     # 🇧🇷 Relatórios | 🇺🇸 Reports
```

---

## 🎯 Tipos de Relatório | Report Types

1.  **🇧🇷 Relatório Técnico Completo | 🇺🇸 Full Technical Report**
2.  **🇧🇷 Seção para Devs Juniores | 🇺🇸 Junior Devs Section**
3.  **🇧🇷 Análise de Viabilidade Comercial | 🇺🇸 Business Viability Analysis**
4.  **🇧🇷 Auditoria Legal | 🇺🇸 Legal Audit**

---

## 🔧 Configuração Avançada | Advanced Configuration

### 📝 **Personalizar Agentes | Customize Agents**

**🇧🇷 Português:** Edite `src/config/agents.yaml`.
**🇺🇸 English:** Edit `src/config/agents.yaml`.

### 🎯 **Métricas Customizadas | Custom Metrics**

**🇧🇷 Português:** Edite `src/config/tasks.yaml`.
**🇺🇸 English:** Edit `src/config/tasks.yaml`.

---

## 📊 Métricas e Outputs | Metrics and Outputs

### 🎯 **Scores**
- Overall Score
- Architecture Score
- Quality Score
- Documentation Score
- Market Readiness
- Legal Compliance
- AI Optimization

---

## 📄 Licença | License

MIT License.
