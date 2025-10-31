#!/usr/bin/env python3
"""
🚀 CrewAI Avaliação Completa V2 - Com Configuração YAML
========================================================

Versão melhorada que usa configuração YAML para agentes e tasks.
Sistema plug-and-play para análise profissional de codebase usando Gemini 2.5 Flash.
"""

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Import custom utilities
from utils.config_loader import load_config

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()


class CodebaseAnalysisCrewV2:
    """
    🤝 CrewAI para Avaliação Completa de Codebase - Versão 2
    
    Usa configuração YAML para definir agentes e tasks.
    Permite fácil customização sem mexer no código.
    """
    
    def __init__(self, gemini_api_key: Optional[str] = None, config_path: Optional[str] = None):
        """
        Inicializa a crew com configuração YAML e Gemini 2.5 Flash
        
        Args:
            gemini_api_key: API key do Gemini (se None, usa GEMINI_API_KEY do .env)
            config_path: Caminho para crew_config.yaml (se None, usa config/crew_config.yaml)
        """
        # Carrega API key
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("❌ GEMINI_API_KEY não encontrada! Configure no .env ou passe como parâmetro")
        
        self.gemini_api_key = self.gemini_api_key.strip()
        logger.info(f"✅ GEMINI_API_KEY carregada: {self.gemini_api_key[:10]}...")
        
        # Configura environment variables para CrewAI
        os.environ["GEMINI_API_KEY"] = self.gemini_api_key
        if "MODEL" not in os.environ:
            os.environ["MODEL"] = "gemini/gemini-2.5-flash"
        
        # Carrega configuração YAML
        try:
            self.config = load_config(config_path)
            logger.info(f"✅ Configuração carregada: {self.config.get_crew_name()}")
        except Exception as e:
            logger.error(f"❌ Erro ao carregar configuração: {e}")
            raise
        
        # Cria agentes e tasks a partir da configuração
        self.agents = self._create_agents_from_config()
        self.tasks = self._create_tasks_from_config()
        
    def _create_agents_from_config(self) -> Dict[str, Agent]:
        """🎭 Cria agentes a partir da configuração YAML"""
        agents = {}
        
        agents_config = self.config.get_all_agents()
        logger.info(f"📋 Criando {len(agents_config)} agentes...")
        
        for agent_key, agent_data in agents_config.items():
            try:
                agent = Agent(
                    role=f"{agent_data.get('emoji', '')} {agent_data['role']}",
                    goal=agent_data['goal'],
                    backstory=agent_data['backstory'],
                    verbose=True,
                    max_iter=agent_data.get('max_iterations', 3),
                    allow_delegation=agent_data.get('delegation', False),
                )
                agents[agent_key] = agent
                logger.info(f"✅ Agente criado: {agent_data['name']}")
            except Exception as e:
                logger.error(f"❌ Erro ao criar agente {agent_key}: {e}")
                raise
        
        return agents
    
    def _create_tasks_from_config(self) -> Dict[str, Task]:
        """📝 Cria tasks a partir da configuração YAML"""
        tasks = {}
        
        tasks_config = self.config.get_all_tasks()
        logger.info(f"📋 Criando {len(tasks_config)} tasks...")
        
        for task_key, task_data in tasks_config.items():
            try:
                # Encontra o agente correspondente
                agent_key = task_data.get('agent')
                if agent_key not in self.agents:
                    logger.warning(f"⚠️ Agente '{agent_key}' não encontrado para task '{task_key}'")
                    continue
                
                task = Task(
                    description=task_data['description'],
                    expected_output=task_data['expected_output'],
                    agent=self.agents[agent_key],
                )
                tasks[task_key] = task
                logger.info(f"✅ Task criada: {task_data['name']}")
            except Exception as e:
                logger.error(f"❌ Erro ao criar task {task_key}: {e}")
                raise
        
        return tasks
    
    def analyze_codebase(self, codebase_report: str, output_file: Optional[str] = None) -> str:
        """
        🔍 Executa análise completa da codebase
        
        Args:
            codebase_report: Relatório inicial da codebase gerado por gerar_relatorio.py
            output_file: Arquivo para salvar o relatório final
            
        Returns:
            Relatório final ultra-profissional
        """
        logger.info("🚀 Iniciando análise completa da codebase...")
        
        # Prepara inputs para as tasks
        inputs = {
            "codebase_report": codebase_report,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Cria crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=list(self.tasks.values()),
            process=Process.sequential,
            verbose=True,
        )
        
        try:
            # Executa análise
            result = crew.kickoff(inputs=inputs)
            logger.info("✅ Análise completa finalizada!")
            
            # Salva resultado
            if output_file:
                self._save_report(result, output_file)
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Erro durante análise: {e}")
            raise
    
    def _save_report(self, result: str, output_file: str):
        """💾 Salva relatório final"""
        try:
            os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            
            logger.info(f"📄 Relatório salvo em: {output_file}")
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar relatório: {e}")
            raise


def main():
    """🎯 Função principal de execução"""
    import sys
    
    print("="*60)
    print("🚀 CrewAI - Avaliação Completa de Codebase V2")
    print("="*60)
    print()
    
    # Verifica health check primeiro
    print("🏥 Recomendação: Execute 'uv run python utils/health_check.py' primeiro")
    print()
    
    # Inicializa crew
    try:
        crew = CodebaseAnalysisCrewV2()
        print(f"✅ Crew '{crew.config.get_crew_name()}' inicializada!")
        print(f"👥 Agentes: {len(crew.agents)}")
        print(f"📝 Tasks: {len(crew.tasks)}")
        print()
    except Exception as e:
        print(f"❌ Erro ao inicializar crew: {e}")
        sys.exit(1)
    
    # Carrega relatório base
    base_report_path = "relatorio_codebase_inicial.md"
    if not os.path.exists(base_report_path):
        print(f"⚠️ Relatório base não encontrado: {base_report_path}")
        print("📝 Execute primeiro: uv run python gerar_relatorio.py .")
        sys.exit(1)
    
    with open(base_report_path, 'r', encoding='utf-8') as f:
        codebase_report = f.read()
    
    print(f"📄 Relatório base carregado ({len(codebase_report)} chars)")
    print()
    
    # Executa análise
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"outputs/reports/relatorio_final_{timestamp}.md"
    
    print("🔍 Iniciando análise completa (isso pode levar alguns minutos)...")
    print()
    
    try:
        result = crew.analyze_codebase(codebase_report, output_file)
        
        print()
        print("="*60)
        print("✅ ANÁLISE COMPLETA!")
        print("="*60)
        print(f"📄 Relatório salvo em: {output_file}")
        print()
        
    except Exception as e:
        print()
        print("="*60)
        print("❌ ERRO NA ANÁLISE")
        print("="*60)
        print(f"Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
