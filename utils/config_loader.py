"""
🔧 Config Loader - Carregador de Configuração YAML
==================================================

Carrega e processa configuração dos agentes e tasks do arquivo YAML.
"""

import yaml
import os
from pathlib import Path
from typing import Dict, Any, Optional, cast
import logging

logger = logging.getLogger(__name__)


class ConfigLoader:
    """Carrega configuração YAML para CrewAI"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Inicializa o loader com caminho da configuração.
        
        Args:
            config_path: Caminho para o arquivo YAML. Se None, usa config/crew_config.yaml
        """
        if config_path is None:
            # Tenta encontrar o arquivo na estrutura do projeto
            possible_paths = [
                Path("config/crew_config.yaml"),
                Path(__file__).parent.parent / "config" / "crew_config.yaml",
            ]
            
            for path in possible_paths:
                if path.exists():
                    config_path = str(path)
                    break
            
            if config_path is None:
                raise FileNotFoundError(
                    "config/crew_config.yaml não encontrado. "
                    "Certifique-se de que o arquivo existe na pasta config/"
                )
        
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Carrega e valida o arquivo YAML"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            logger.info(f"✅ Configuração carregada de: {self.config_path}")
            return cast(Dict[str, Any], config)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao parsear YAML: {e}")
    
    def get_llm_config(self) -> Dict[str, Any]:
        """Retorna configuração do LLM"""
        return cast(Dict[str, Any], self.config.get('crew_config', {}).get('llm_config', {}))
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """
        Retorna configuração de um agente específico.
        
        Args:
            agent_name: Nome do agente (ex: 'arquiteto_software')
            
        Returns:
            Dicionário com role, goal, backstory, etc.
        """
        agents = self.config.get('agents', {})
        if agent_name not in agents:
            raise ValueError(f"Agente '{agent_name}' não encontrado na configuração")
        
        return cast(Dict[str, Any], agents[agent_name])
    
    def get_task_config(self, task_name: str) -> Dict[str, Any]:
        """
        Retorna configuração de uma task específica.
        
        Args:
            task_name: Nome da task (ex: 'analise_arquitetural')
            
        Returns:
            Dicionário com description, expected_output, etc.
        """
        tasks = self.config.get('tasks', {})
        if task_name not in tasks:
            raise ValueError(f"Task '{task_name}' não encontrada na configuração")
        
        return cast(Dict[str, Any], tasks[task_name])
    
    def get_all_agents(self) -> Dict[str, Dict[str, Any]]:
        """Retorna configuração de todos os agentes"""
        return cast(Dict[str, Dict[str, Any]], self.config.get('agents', {}))
    
    def get_all_tasks(self) -> Dict[str, Dict[str, Any]]:
        """Retorna configuração de todas as tasks"""
        return cast(Dict[str, Dict[str, Any]], self.config.get('tasks', {}))
    
    def get_metrics_config(self) -> Dict[str, Any]:
        """Retorna configuração de métricas e thresholds"""
        return cast(Dict[str, Any], self.config.get('metrics', {}))
    
    def get_operational_settings(self) -> Dict[str, Any]:
        """Retorna configurações operacionais"""
        return cast(Dict[str, Any], self.config.get('operational_settings', {}))
    
    def get_crew_name(self) -> str:
        """Retorna nome da crew"""
        return cast(str, self.config.get('crew_config', {}).get('name', 'CrewAI'))
    
    def get_crew_description(self) -> str:
        """Retorna descrição da crew"""
        return cast(str, self.config.get('crew_config', {}).get('description', ''))


def load_config(config_path: Optional[str] = None) -> ConfigLoader:
    """
    Helper function para carregar configuração.
    
    Args:
        config_path: Caminho opcional para o arquivo YAML
        
    Returns:
        Instância de ConfigLoader
        
    Example:
        >>> config = load_config()
        >>> arquiteto = config.get_agent_config('arquiteto_software')
        >>> print(arquiteto['role'])
        'Arquiteto de Software Sênior'
    """
    return ConfigLoader(config_path)


if __name__ == "__main__":
    # Teste do config loader
    try:
        config = load_config()
        print("✅ Config carregada com sucesso!")
        print(f"📋 Crew: {config.get_crew_name()}")
        print(f"👥 Agentes disponíveis: {list(config.get_all_agents().keys())}")
        print(f"📝 Tasks disponíveis: {list(config.get_all_tasks().keys())}")
    except Exception as e:
        print(f"❌ Erro: {e}")
