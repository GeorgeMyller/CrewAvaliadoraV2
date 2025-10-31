#!/usr/bin/env python3
"""
🚀 CrewAI Avaliação Completa de Codebase
========================================

Sistema plug-and-play para análise profissional de codebase usando Gemini 2.5 Flash.
Gera relatórios ultra-profissionais para devs juniores e seniores.

Fluxo: Codebase → Script Python → Relatório → CrewAI → Relatório Ultra-Profissional
"""

from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool, DirectoryReadTool
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

class CodebaseAnalysisCrew:
    """
    🤝 CrewAI para Avaliação Completa de Codebase
    
    Roles especializados:
    📐 Arquiteto de Software
    🧪 Engenheiro de Qualidade  
    📄 Documentador Técnico
    🚀 Product Manager
    ⚖️ Especialista Legal
    🤖 Engenheiro de IA
    """
    
    def __init__(self, gemini_api_key: Optional[str] = None):
        """Inicializa a crew com configuração Gemini 2.5 Flash"""
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("❌ GEMINI_API_KEY não encontrada! Configure no .env")
            
        # Configuração otimizada do Gemini 2.5 Flash
        self.llm = LLM(
            model="google/gemini-2.5-flash",
            api_key=self.gemini_api_key,
            temperature=0.3,  # Análise mais focada
            max_tokens=8192,  # Máximo para respostas detalhadas
        )
        
        # Tools para leitura de arquivos
        self.file_tool = FileReadTool()
        self.dir_tool = DirectoryReadTool()
        
        # Cria agentes especializados
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        
    def _create_agents(self) -> Dict[str, Agent]:
        """🎭 Cria todos os agentes especializados"""
        
        agents = {
            # 📐 Arquiteto de Software
            "arquiteto": Agent(
                role="🏗️ Arquiteto de Software Sênior",
                goal="""Analisar profundamente a arquitetura da aplicação, identificando:
                - Padrões arquiteturais usados (MVC, Clean Architecture, etc.)
                - Qualidade das integrações com APIs externas
                - Escalabilidade e manutenibilidade do código
                - Pontos de falha e gargalos potenciais
                - Sugestões concretas de refatoração""",
                backstory="""Arquiteto de software com 10+ anos de experiência em sistemas distribuídos,
                APIs de redes sociais e automação. Especialista em Instagram Graph API v23, WhatsApp Business API
                e arquiteturas para SaaS. Conhece profundamente padrões como Repository, Factory, Observer e
                estratégias de rate limiting para APIs.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            ),
            
            # 🧪 Engenheiro de Qualidade
            "qa_engineer": Agent(
                role="🔬 Engenheiro de Qualidade e Testes",
                goal="""Avaliar rigorosamente a qualidade do código:
                - Cobertura de testes (unitários, integração, E2E)
                - Análise estática de código (complexity, duplication)
                - Práticas de CI/CD e deployment
                - Identificação de bugs e vulnerabilidades
                - Estratégias de monitoramento e observabilidade""",
                backstory="""Engenheiro de QA com expertise em automação de testes, análise estática
                e pipelines CI/CD. Experiência com pytest, bandit, ruff e ferramentas de segurança.
                Especialista em testes de APIs, mock de serviços externos e estratégias de teste para
                sistemas que integram redes sociais.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            ),
            
            # 📄 Documentador Técnico
            "documentador": Agent(
                role="📚 Documentador Técnico Sênior",
                goal="""Garantir documentação de classe mundial:
                - Clareza para onboarding de desenvolvedores
                - Completude da documentação de APIs
                - Guias de instalação e configuração
                - Exemplos práticos e troubleshooting
                - Documentação de arquitetura e decisões técnicas""",
                backstory="""Documentador técnico especializado em projetos open-source e SaaS.
                Expert em criar documentação que funciona para diferentes níveis técnicos,
                desde devs juniores até arquitetos seniores. Conhece ferramentas como Sphinx,
                MkDocs e padrões de documentação de APIs REST.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            ),
            
            # 🚀 Product Manager
            "product_manager": Agent(
                role="🎯 Product Manager Estratégico",
                goal="""Avaliar viabilidade comercial e estratégica:
                - Prontidão para lançamento como SaaS
                - Análise competitiva e diferenciação
                - Roadmap de features e priorização
                - Estratégia de monetização
                - Riscos de adoção e go-to-market""",
                backstory="""Product Manager com 8+ anos em produtos de automação e marketing digital.
                Experiência em lançar SaaS para redes sociais, conhece profundamente o mercado de
                automação Instagram/WhatsApp. Expert em definir MVP, pricing strategy e user journey
                para produtos B2B.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            ),
            
            # ⚖️ Especialista Legal
            "especialista_legal": Agent(
                role="⚖️ Consultor Jurídico de Tecnologia",
                goal="""Assegurar conformidade legal total:
                - Compliance com termos das APIs (Instagram, WhatsApp)
                - Conformidade LGPD/GDPR para dados pessoais
                - Riscos legais de automação em redes sociais
                - Políticas de uso e termos de serviço
                - Estratégias de mitigação de riscos legais""",
                backstory="""Advogado especializado em direito digital com foco em APIs de redes sociais.
                Expert em LGPD, GDPR e regulamentações de automação. Experiência em revisar contratos
                de APIs, políticas de uso de dados e compliance para startups de tecnologia.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            ),
            
            # 🤖 Engenheiro de IA
            "engenheiro_ia": Agent(
                role="🧠 Engenheiro de IA Especialista",
                goal="""Otimizar componentes de inteligência artificial:
                - Análise do pipeline de geração de legendas
                - Otimização de prompts e modelos LLM
                - Estratégias de personalização por usuário
                - Performance e custos de APIs de IA
                - Implementação de RAG e fine-tuning""",
                backstory="""Engenheiro de IA com especialização em NLP, visão computacional e LLMs.
                Experiência com Google Gemini, OpenAI GPT, e modelos de visão para análise de imagens.
                Expert em otimização de prompts, RAG systems e estratégias de personalização de conteúdo
                para redes sociais.""",
                tools=[self.file_tool, self.dir_tool],
                llm=self.llm,
                verbose=True,
                max_iter=3,
                allow_delegation=False
            )
        }
        
        return agents
    
    def _create_tasks(self) -> List[Task]:
        """📋 Cria tasks específicas para cada agente"""
        
        tasks = [
            # Task do Arquiteto
            Task(
                description="""📐 ANÁLISE ARQUITETURAL COMPLETA
                
                Leia o arquivo 'relatorio_codebase_turbinado.md' e conduza uma análise arquitetural profunda:
                
                1. **Arquitetura Atual**: Descreva o padrão arquitetural identificado
                2. **Integrações**: Analise as integrações com APIs externas (Instagram, WhatsApp, Gemini)
                3. **Fluxo de Dados**: Mapeie o fluxo de dados de ponta a ponta
                4. **Escalabilidade**: Identifique gargalos e pontos de falha
                5. **Padrões de Design**: Liste padrões usados e ausentes
                6. **Refatorações Sugeridas**: Proponha melhorias concretas com priorização
                
                Foque em aspectos técnicos profundos e seja específico nas recomendações.""",
                expected_output="""Análise arquitetural estruturada em seções:
                - Resumo da arquitetura atual
                - Qualidade das integrações
                - Pontos críticos identificados
                - Recomendações priorizadas (Alta/Média/Baixa)
                - Diagrama conceitual em texto
                """,
                agent=self.agents["arquiteto"]
            ),
            
            # Task do QA Engineer
            Task(
                description="""🧪 AVALIAÇÃO DE QUALIDADE E TESTES
                
                Analise o relatório focando em qualidade de código e estratégias de teste:
                
                1. **Cobertura de Testes**: Avalie testes existentes (unitários, integração, E2E)
                2. **Qualidade do Código**: Analise complexity, duplicação, code smells
                3. **Segurança**: Identifique vulnerabilidades e riscos de segurança
                4. **CI/CD Pipeline**: Avalie práticas de deployment e automação
                5. **Monitoramento**: Analise estratégias de logging e observabilidade
                6. **Plano de Testes**: Sugira estratégia completa de testes
                
                Seja específico em métricas e ferramentas recomendadas.""",
                expected_output="""Relatório de qualidade estruturado:
                - Score de qualidade atual (0-100)
                - Gaps críticos em testes
                - Vulnerabilidades identificadas
                - Estratégia de testes recomendada
                - Ferramentas e métricas sugeridas
                - Roadmap de melhorias em qualidade
                """,
                agent=self.agents["qa_engineer"]
            ),
            
            # Task do Documentador
            Task(
                description="""📄 AUDITORIA DE DOCUMENTAÇÃO
                
                Avalie a completude e qualidade da documentação existente:
                
                1. **Documentação de Usuário**: Avalie clareza para usuários finais
                2. **Documentação Técnica**: Analise docs para desenvolvedores
                3. **API Documentation**: Verifique documentação de endpoints
                4. **Onboarding**: Avalie facilidade de setup para novos devs
                5. **Exemplos Práticos**: Analise qualidade dos exemplos
                6. **Manutenção**: Avalie processo de atualização da documentação
                
                Priorize aspectos que impactam adoção e produtividade.""",
                expected_output="""Auditoria de documentação:
                - Score de completude (0-100)
                - Gaps críticos identificados
                - Sugestões de reorganização
                - Templates recomendados
                - Estratégia de manutenção
                - Roadmap de melhorias documentais
                """,
                agent=self.agents["documentador"]
            ),
            
            # Task do Product Manager
            Task(
                description="""🚀 ANÁLISE DE VIABILIDADE COMERCIAL
                
                Avalie a prontidão do produto para o mercado:
                
                1. **Market Readiness**: Analise maturidade para lançamento SaaS
                2. **Competitive Analysis**: Compare com soluções existentes
                3. **Value Proposition**: Identifique diferenciadores únicos
                4. **User Journey**: Mapeie jornada do usuário ideal
                5. **Monetization**: Sugira modelos de precificação
                6. **Go-to-Market**: Proponha estratégia de lançamento
                
                Foque em aspectos que impactam success comercial.""",
                expected_output="""Análise comercial estratégica:
                - Score de prontidão para mercado (0-100)
                - Análise competitiva resumida
                - Proposta de valor única
                - Roadmap de lançamento em fases
                - Modelo de monetização sugerido
                - Riscos comerciais e mitigações
                """,
                agent=self.agents["product_manager"]
            ),
            
            # Task do Especialista Legal
            Task(
                description="""⚖️ ANÁLISE DE CONFORMIDADE LEGAL
                
                Conduza uma auditoria legal completa do projeto:
                
                1. **API Terms Compliance**: Analise conformidade com termos das APIs
                2. **Data Privacy**: Avalie conformidade LGPD/GDPR
                3. **Automation Risks**: Identifique riscos legais de automação
                4. **Terms of Service**: Sugira política de uso adequada
                5. **Liability Issues**: Mapeie responsabilidades e riscos
                6. **Compliance Strategy**: Proponha plano de conformidade
                
                Priorize riscos que podem impactar operação ou lançamento.""",
                expected_output="""Relatório de conformidade legal:
                - Score de compliance (0-100)
                - Riscos legais críticos
                - Não conformidades identificadas
                - Plano de adequação legal
                - Políticas necessárias
                - Roadmap de compliance
                """,
                agent=self.agents["especialista_legal"]
            ),
            
            # Task do Engenheiro de IA
            Task(
                description="""🤖 OTIMIZAÇÃO DO PIPELINE DE IA
                
                Analise e otimize os componentes de inteligência artificial:
                
                1. **LLM Integration**: Avalie uso atual do Gemini e outros LLMs
                2. **Prompt Engineering**: Analise qualidade dos prompts
                3. **Performance**: Avalie latência e custos de APIs de IA
                4. **Personalization**: Sugira estratégias de personalização
                5. **Model Selection**: Avalie adequação dos modelos escolhidos
                6. **AI Strategy**: Proponha roadmap de melhorias em IA
                
                Foque em otimizações que impactam UX e custos operacionais.""",
                expected_output="""Análise de IA estratégica:
                - Score de otimização IA (0-100)
                - Bottlenecks identificados
                - Oportunidades de melhoria
                - Estratégia de personalização
                - Otimizações de custo sugeridas
                - Roadmap de evolução IA
                """,
                agent=self.agents["engenheiro_ia"]
            )
        ]
        
        return tasks
    
    def create_final_report_task(self) -> Task:
        """📑 Cria task final para consolidação do relatório"""
        
        return Task(
            description="""🎯 CONSOLIDAÇÃO DO RELATÓRIO FINAL
            
            Com base em todas as análises anteriores, crie um relatório ultra-profissional com:
            
            ## 📊 ESTRUTURA DO RELATÓRIO FINAL:
            
            ### 🎯 EXECUTIVE SUMMARY
            - Score geral do projeto (0-100)
            - Principais forças e fraquezas
            - Recomendação de go/no-go
            
            ### 👶 SEÇÃO PARA DEVS JUNIORES
            - Explicação simples da arquitetura
            - Conceitos técnicos com analogias
            - Passos claros para contribuir
            - Recursos de aprendizado
            
            ### 🚀 SEÇÃO PARA DEVS SENIORES
            - Análise técnica profunda
            - Diagramas e fluxos detalhados
            - Decisões arquiteturais críticas
            - Trade-offs e justificativas
            
            ### 📈 ROADMAP ESTRATÉGICO
            - Fase 1: Correções críticas (0-3 meses)
            - Fase 2: Melhorias estruturais (3-6 meses)  
            - Fase 3: Expansão e otimização (6-12 meses)
            
            ### ⚡ QUICK WINS
            - Ações de alto impacto e baixo esforço
            - Implementações imediatas
            
            ### 🚨 RISCOS CRÍTICOS
            - Top 5 riscos priorizados
            - Planos de mitigação
            
            Use markdown profissional com emojis, tabelas e formatação clara.""",
            expected_output="""Relatório final em markdown com:
            - Executive summary executivo
            - Seções para diferentes públicos
            - Roadmap detalhado e priorizado
            - Métricas e scores quantitativos
            - Recomendações acionáveis
            - Formatação profissional
            """,
            agent=self.agents["arquiteto"],  # Arquiteto como consolidador final
            context=self.tasks  # Recebe contexto de todas as tasks anteriores
        )
    
    def run_analysis(self, report_path: str = "relatorio_codebase_turbinado.md") -> str:
        """🚀 Executa análise completa da codebase"""
        
        logger.info("🚀 Iniciando análise completa da codebase...")
        
        # Verifica se o relatório de entrada existe
        if not os.path.exists(report_path):
            raise FileNotFoundError(f"❌ Relatório não encontrado: {report_path}")
        
        # Adiciona task final de consolidação
        all_tasks = self.tasks + [self.create_final_report_task()]
        
        # Configura a crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=all_tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
        )
        
        # Executa a análise
        try:
            logger.info("🔄 Executando análise com CrewAI...")
            result = crew.kickoff()
            
            # Salva resultado
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"relatorio_final_startup_{timestamp}.md"
            
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(str(result))
            
            # Cria também uma versão JSON com metadados
            metadata = {
                "timestamp": timestamp,
                "input_file": report_path,
                "output_file": output_file,
                "agents_used": list(self.agents.keys()),
                "total_tasks": len(all_tasks),
                "llm_model": "gemini-2.5-flash"
            }
            
            metadata_file = f"metadata_analise_{timestamp}.json"
            with open(metadata_file, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.info("✅ Análise concluída!")
            logger.info(f"📄 Relatório salvo em: {output_file}")
            logger.info(f"📊 Metadados salvos em: {metadata_file}")
            
            return output_file
            
        except Exception as e:
            logger.error(f"❌ Erro durante análise: {str(e)}")
            raise


def main():
    """🎯 Função principal para execução direta"""
    
    print("🚀 CrewAI - Análise Completa de Codebase")
    print("=" * 50)
    
    try:
        # Inicializa a crew
        crew_analyzer = CodebaseAnalysisCrew()
        
        # Executa análise
        report_path = "relatorio_codebase_turbinado.md"
        if not os.path.exists(report_path):
            print(f"⚠️  Relatório '{report_path}' não encontrado!")
            print("💡 Execute primeiro o script de geração de relatório.")
            return
        
        output_file = crew_analyzer.run_analysis(report_path)
        
        print("\n🎉 Análise concluída com sucesso!")
        print(f"📄 Relatório final: {output_file}")
        print("\n👀 Visualize o relatório com:")
        print(f"   cat {output_file}")
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
