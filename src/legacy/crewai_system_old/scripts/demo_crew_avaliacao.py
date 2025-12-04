#!/usr/bin/env python3
"""
🧪 DEMO - CrewAI Avaliação de Codebase
=====================================

Script de demonstração da crew de avaliação.
Simula o fluxo completo com dados mockados para teste.
"""

import os
import sys
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()


def create_demo_report():
    """📄 Cria um relatório de exemplo para demonstração"""

    demo_content = f"""# 📊 Relatório Turbinado da Codebase - DEMO
## Agent Social Media - Automação WhatsApp→Instagram

### 📅 Informações Básicas
- **Data de análise**: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
- **Projeto**: Agent Social Media
- **Linguagem principal**: Python 3.12
- **Framework**: CrewAI + Flask + Docker

### 🏗️ Arquitetura do Sistema

#### Componentes Principais:
1. **Core Engine** (`src/core/`): Lógica principal de automação
2. **API Integrations** (`src/integrations/`): WhatsApp, Instagram, Gemini
3. **AI Pipeline** (`src/ai/`): Processamento de imagens e geração de legendas
4. **Web Dashboard** (`src/web/`): Interface de usuário
5. **Queue System** (`src/queues/`): Celery + Redis para processamento assíncrono

#### Fluxo de Dados:
```
WhatsApp Message → Queue → AI Processing → Instagram Post
                     ↓
              Redis Storage ← → Dashboard UI
```

### 📊 Métricas da Codebase
- **Total de arquivos**: 156
- **Linhas de código**: 15,420
- **Arquivos Python**: 89
- **Arquivos de configuração**: 23
- **Testes**: 12 arquivos (coverage: 35%)

### 🔧 Tecnologias Utilizadas

#### Backend:
- CrewAI 0.130.0 (Agentes de IA)
- Flask 3.1.0 (API REST)
- Celery 5.3.0 (Queue de tarefas)
- Redis 5.0.0 (Cache e filas)

#### IA e Processamento:
- Google Gemini 2.5 Flash (Geração de texto)
- Pillow 11.1.0 (Processamento de imagens)
- MoviePy 1.0.3 (Processamento de vídeos)

#### Infraestrutura:
- Docker + Docker Compose
- Nginx (Proxy reverso)
- PostgreSQL (Dados persistentes)

### 🔌 Integrações de APIs

#### 1. WhatsApp Business API
- **Status**: ✅ Funcionando
- **Rate Limit**: 1000/min
- **Webhooks**: Configurados
- **Autenticação**: Token Bearer

#### 2. Instagram Graph API v23
- **Status**: ✅ Funcionando  
- **Rate Limit**: 200/hora
- **Permissions**: publish_content, read_insights
- **Compliance**: Revisar ToS

#### 3. Google Gemini API
- **Status**: ✅ Funcionando
- **Modelo**: gemini-2.5-flash
- **Rate Limit**: 1500/min
- **Custo mensal estimado**: $150-300

### 🧪 Qualidade e Testes

#### Cobertura de Testes:
- **Unitários**: 25% (Target: 80%)
- **Integração**: 10% (Target: 60%)
- **E2E**: 0% (Target: 40%)

#### Análise Estática:
- **Complexity Score**: 7.2/10
- **Duplicação**: 8%
- **Security Issues**: 7 (2 High, 5 Medium)
- **Code Smells**: 23

### 📝 Documentação Atual

#### Pontos Fortes:
- ✅ README principal bem estruturado
- ✅ Docker setup documentado
- ✅ Variáveis de ambiente listadas

#### Gaps Identificados:
- ❌ Falta API documentation
- ❌ Onboarding guide incompleto
- ❌ Troubleshooting guide ausente
- ❌ Contribuição guidelines básicos

### 🚀 Estado do Produto

#### Features Implementadas:
- [x] Recepção de mensagens WhatsApp
- [x] Processamento de imagens com filtros
- [x] Geração de legendas com IA
- [x] Publicação automática no Instagram
- [x] Dashboard web básico
- [x] Sistema de filas

#### Features em Desenvolvimento:
- [ ] Agendamento de posts
- [ ] Analytics e métricas
- [ ] Multi-usuário
- [ ] API pública

### ⚖️ Aspectos Legais

#### Compliance Atual:
- ⚠️ Termos de uso das APIs: Revisar
- ⚠️ LGPD: Política de privacidade incompleta
- ⚠️ Disclaimer: Ausente
- ⚠️ Data retention: Não definido

#### Riscos Identificados:
1. Automação pode violar ToS do Instagram
2. Dados pessoais sem proteção adequada
3. Ausência de consentimento explícito
4. Logs podem conter informações sensíveis

### 🤖 Pipeline de IA

#### Componentes:
1. **Image Analysis**: Detecção de objetos, cores, mood
2. **Content Generation**: Prompts para Gemini
3. **Style Personalization**: Adaptação por usuário
4. **Quality Control**: Filtros de qualidade

#### Performance Atual:
- **Tempo médio geração**: 12s
- **Taxa de sucesso**: 87%
- **Qualidade percebida**: 7.2/10
- **Custo por geração**: $0.04

### 🔧 Infraestrutura

#### Deployment:
- **Container**: Docker + Compose
- **Proxy**: Nginx
- **SSL**: Let's Encrypt
- **Monitoring**: Básico (logs)

#### Escalabilidade:
- **Current capacity**: ~50 usuários simultâneos
- **Bottlenecks**: Rate limits de APIs, processamento single-thread
- **Scaling strategy**: Horizontal com load balancer

### 📈 Próximos Passos Identificados

#### Crítico (0-1 mês):
1. Implementar testes de integração
2. Auditoria legal completa
3. Setup de monitoramento
4. Correções de segurança

#### Importante (1-3 meses):
1. Documentação completa
2. Multi-tenancy
3. Analytics dashboard
4. Performance optimization

#### Desejável (3-6 meses):
1. Mobile app
2. API pública
3. Marketplace de templates
4. Integração com outras redes sociais

---

**📊 Este é um relatório de demonstração gerado automaticamente**  
**🔄 Para análise real, execute: python gerar_relatorio.py [caminho]**"""

    with open("relatorio_codebase_turbinado.md", "w", encoding="utf-8") as f:
        f.write(demo_content)

    print("📄 Relatório demo criado: relatorio_codebase_turbinado.md")
    return "relatorio_codebase_turbinado.md"


def test_gemini_connection():
    """🧪 Testa conexão com Gemini API"""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY não configurada!")
        print("💡 Configure no arquivo .env:")
        print("   GEMINI_API_KEY=sua_chave_aqui")
        return False

    try:
        # Teste simples sem importar a biblioteca completa
        print("✅ Gemini API Key configurada!")
        print("📝 Teste de conexão será feito durante execução da crew...")
        return True

    except Exception as e:
        print(f"❌ Erro na conexão com Gemini: {str(e)}")
        return False


def run_demo_crew():
    """🤖 Executa demo da crew"""

    print("🚀 DEMO - CrewAI Avaliação de Codebase")
    print("=" * 50)

    # 1. Verifica dependências
    print("🔍 Verificando dependências...")
    try:
        from crew_avaliacao_completa import CodebaseAnalysisCrew

        print("✅ CrewAI classes importadas com sucesso!")
    except ImportError as e:
        print(f"❌ Erro ao importar: {str(e)}")
        print("💡 Execute: uv add crewai crewai-tools")
        return False

    # 2. Testa conexão Gemini
    if not test_gemini_connection():
        return False

    # 3. Cria relatório demo
    print("\n📄 Gerando relatório demo...")
    demo_report = create_demo_report()

    # 4. Executa crew
    print("\n🤖 Executando análise da crew...")
    try:
        crew_analyzer = CodebaseAnalysisCrew()
        output_file = crew_analyzer.run_analysis(demo_report)

        print("\n🎉 Demo concluída com sucesso!")
        print(f"📄 Relatório final: {output_file}")

        # 5. Mostra preview do resultado
        if os.path.exists(output_file):
            print("\n👀 Preview do relatório:")
            print("-" * 40)
            with open(output_file, encoding="utf-8") as f:
                content = f.read()
                # Mostra primeiras linhas
                lines = content.split("\n")[:20]
                for line in lines:
                    print(line)
                print("...")
                print(f"\n📖 Arquivo completo: {output_file}")

        return True

    except Exception as e:
        print(f"❌ Erro na execução da crew: {str(e)}")
        return False


def main():
    """🎯 Função principal do demo"""

    if len(sys.argv) > 1 and sys.argv[1] == "--setup":
        print("🔧 Configurando demo...")

        # Verifica se .env existe
        if not os.path.exists(".env"):
            print("📝 Criando arquivo .env de exemplo...")
            with open(".env", "w") as f:
                f.write("# Configuração para CrewAI Demo\n")
                f.write("GEMINI_API_KEY=your_gemini_key_here\n")
                f.write("# Obtenha sua chave em: https://aistudio.google.com/app/apikey\n")

            print("✅ Arquivo .env criado!")
            print("🔑 Configure sua GEMINI_API_KEY no arquivo .env")
            return 0

        print("✅ Setup concluído!")
        return 0

    # Executa demo
    success = run_demo_crew()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
