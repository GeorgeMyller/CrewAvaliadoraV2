# 🚀 CrewAvaliadora - Arquitetura do Sistema | System Architecture

## 🇧🇷 Português

### 📋 Visão Geral

Sistema plug-and-play que utiliza **6 especialistas IA** para gerar análises profissionais de codebase usando **Gemini 2.5 Flash**.

### 🎯 Fluxo Completo

```
📂 Codebase → 🐍 Script Análise → 📄 Relatório → 🤝 CrewAI → 📑 Relatório Ultra-Profissional
```

---

## 🇺🇸 English

### 📋 Overview

Plug-and-play system that uses **6 AI specialists** to generate professional codebase analysis using **Gemini 2.5 Flash**.

### 🎯 Complete Flow

```
📂 Codebase → 🐍 Analysis Script → 📄 Report → 🤝 CrewAI → 📑 Ultra-Professional Report
```

---

## 🎭 Especialistas da Crew | Crew Specialists

| 🇧🇷 Agente | 🇺🇸 Agent | 🎯 Foco | Focus |
|-----------|----------|---------|-------|
| 📐 **Arquiteto de Software** | **Software Architect** | Arquitetura & Design Patterns | Architecture & Design Patterns |
| 🧪 **Engenheiro de Qualidade** | **QA Engineer** | Testes & Qualidade | Testing & Quality |
| 📄 **Documentador Técnico** | **Technical Writer** | Documentação & Onboarding | Documentation & Onboarding |
| 🚀 **Product Manager** | **Product Manager** | Viabilidade Comercial | Business Viability |
| ⚖️ **Especialista Legal** | **Legal Specialist** | Compliance & Riscos | Compliance & Risks |
| 🤖 **Engenheiro de IA** | **AI Engineer** | Otimização de LLMs | LLM Optimization |

## 📁 Estrutura dos Arquivos | File Structure

```
CrewAvaliadora/
├── src/
│   ├── analyze_repo.py          # 🇧🇷 Lógica de análise | 🇺🇸 Analysis logic
│   ├── streamlit_app.py         # 🇧🇷 Interface Web | 🇺🇸 Web Interface
│   ├── config/                  # 🇧🇷 Configurações | 🇺🇸 Configuration
│   ├── crew/                    # 🇧🇷 Definição dos Agentes | 🇺🇸 Agent Definitions
│   ├── security/                # 🇧🇷 Segurança | 🇺🇸 Security
│   ├── tools/                   # 🇧🇷 Ferramentas | 🇺🇸 Tools
│   └── utils/                   # 🇧🇷 Utilitários | 🇺🇸 Utilities
├── docs/                        # 🇧🇷 Documentação | 🇺🇸 Documentation
├── outputs/                     # 🇧🇷 Relatórios gerados | 🇺🇸 Generated reports
├── tests/                       # 🇧🇷 Testes | 🇺🇸 Test suite
└── pyproject.toml               # 🇧🇷 Dependências | 🇺🇸 Dependencies
```

### 🎯 Componentes Principais | Key Components

**🇧🇷 Português:**
- **src/analyze_repo.py**: Orquestrador principal da análise.
- **src/streamlit_app.py**: Interface gráfica para facilitar o uso.
- **src/crew/**: Contém a lógica dos agentes CrewAI.
- **src/tools/**: Ferramentas personalizadas para os agentes.

**🇺🇸 English:**
- **src/analyze_repo.py**: Main analysis orchestrator.
- **src/streamlit_app.py**: Graphical interface for ease of use.
- **src/crew/**: Contains CrewAI agent logic.
- **src/tools/**: Custom tools for agents.

## 🎯 Tipos de Relatório Gerados | Generated Report Types

### 📊 1. Relatório Técnico Completo | Full Technical Report
- **🇧🇷 Público**: Desenvolvedores seniores, arquitetos
- **🇺🇸 Audience**: Senior developers, architects
- **🇧🇷 Conteúdo**: Análise arquitetural profunda, métricas de qualidade
- **🇺🇸 Content**: Deep architectural analysis, quality metrics

### 👶 2. Seção para Devs Juniores | Junior Devs Section
- **🇧🇷 Público**: Desenvolvedores iniciantes
- **🇺🇸 Audience**: Junior developers
- **🇧🇷 Conteúdo**: Explicações simples, passos de contribuição
- **🇺🇸 Content**: Simple explanations, contribution steps

### 🚀 3. Análise de Viabilidade Comercial | Business Viability Analysis
- **🇧🇷 Público**: Product Managers, stakeholders
- **🇺🇸 Audience**: Product Managers, stakeholders
- **🇧🇷 Conteúdo**: Market readiness, roadmap
- **🇺🇸 Content**: Market readiness, roadmap

### ⚖️ 4. Auditoria Legal | Legal Audit
- **🇧🇷 Público**: Legal team, compliance officers
- **🇺🇸 Audience**: Legal team, compliance officers
- **🇧🇷 Conteúdo**: Riscos LGPD/GDPR, compliance
- **🇺🇸 Content**: LGPD/GDPR risks, compliance

## 🔧 Configuração Avançada | Advanced Configuration

### 📝 Personalizar Agentes | Customize Agents

**🇧🇷 Português:**
Edite `src/config/agents.yaml` para ajustar comportamentos.

**🇺🇸 English:**
Edit `src/config/agents.yaml` to adjust behaviors.

### 🎯 Métricas Customizadas | Custom Metrics

**🇧🇷 Português:**
Defina métricas em `src/config/tasks.yaml`.

**🇺🇸 English:**
Define metrics in `src/config/tasks.yaml`.

## 📊 Métricas e Outputs | Metrics and Outputs

### 🎯 Scores Gerados | Generated Scores
- **Overall Score**: 0-100
- **Architecture Score**
- **Quality Score**
- **Documentation Score**
- **Market Readiness**
- **Legal Compliance**
- **AI Optimization**

### 📄 Arquivos de Output | Output Files
```
outputs/
├── reports/
│   └── relatorio_final_{project}.md
├── metadata/
│   └── metadata_{project}.json
└── logs/
```
