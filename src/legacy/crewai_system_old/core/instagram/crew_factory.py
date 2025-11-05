"""

Módulo crew_factory
-------------------
Este módulo fornece uma fábrica para criar instâncias de CrewAI personalizadas para grupos do Instagram, 
baseando-se em configurações armazenadas em um arquivo JSON. Permite carregar, acessar e atualizar 
configurações de grupos, além de fornecer utilitários para obter instâncias configuradas e listar grupos disponíveis.
Classes:
--------
CrewFactory
    Fábrica responsável por criar instâncias de AdvancedInstagramPostCrew conforme a configuração de cada grupo.
    - __init__(config_path: Optional[str] = None): Inicializa a fábrica com o caminho do arquivo de configuração.
    - create_crew_for_group(group_id: str): Cria uma instância de CrewAI para um grupo específico.
    - get_available_groups(): Retorna os grupos ativos disponíveis.
    - get_group_config(group_id: str): Retorna a configuração completa de um grupo.
    - refresh_configs(): Recarrega as configurações dos grupos.
Variáveis Globais:
------------------
crew_factory
    Instância global da CrewFactory para uso em todo o sistema.
Funções Utilitárias:
--------------------
get_crew_for_group(group_id: str)
    Obtém uma instância de CrewAI para um grupo específico.
get_available_groups()
    Retorna os grupos ativos disponíveis.
refresh_group_configs()
    Recarrega as configurações dos grupos.
Exemplo de Uso:
---------------
Ao executar o módulo diretamente, são listados os grupos disponíveis e testada a criação de CrewAI para cada grupo, 
mostrando informações do perfil configurado.
Dependências:
-------------
- json
- logging
- typing
- pathlib
- advanced_crew_post_instagram.AdvancedInstagramPostCrew

"""

import json
import os
import re
import logging
from typing import Dict, Any, Optional
from pathlib import Path

from .advanced_crew_post_instagram import AdvancedInstagramPostCrew

logger = logging.getLogger(__name__)


class CrewFactory:
    """
    Factory para criar instâncias de CrewAI baseadas na configuração do grupo
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Inicializa o factory com o caminho para as configurações dos grupos
        
        Args:
            config_path: Caminho para o arquivo group_configs.json
        """
        if config_path is None:
            # Buscar o arquivo de configuração no diretório padrão
            base_dir = Path(__file__).parent.parent.parent.parent.parent
            self.config_path = base_dir / "config" / "environments" / "group_configs.json"
        else:
            self.config_path = Path(config_path)
        
        self._group_configs = self._load_group_configs()
    
    def _load_group_configs(self) -> Dict[str, Any]:
        """Carrega as configurações dos grupos"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    raw_config = json.load(f)
                    # Resolver variáveis de ambiente
                    return self._resolve_env_variables(raw_config)
            else:
                logger.warning(f"⚠️  Arquivo de configuração não encontrado: {self.config_path}")
                return {}
        except Exception as e:
            logger.error(f"❌ Erro ao carregar configurações: {str(e)}")
            return {}

    def _resolve_env_variables(self, config_data: Dict) -> Dict:
        """
        Resolve variáveis de ambiente no formato ${VAR_NAME} ou $VAR_NAME
        
        Args:
            config_data: Dicionário com configurações que podem conter referências ENV
            
        Returns:
            Dicionário com variáveis resolvidas
        """
        resolved_config = {}
        
        for key, value in config_data.items():
            if isinstance(value, str):
                # Procurar por padrões ${VAR_NAME} ou $VAR_NAME
                pattern = r'\$\{([^}]+)\}|\$([A-Z_][A-Z0-9_]*)'
                
                def replace_env_var(match):
                    # Capturar nome da variável (grupo 1 para ${VAR} ou grupo 2 para $VAR)
                    var_name = match.group(1) or match.group(2)
                    
                    # Tentar obter valor da variável de ambiente
                    env_value = os.getenv(var_name)
                    
                    if env_value is not None:
                        return env_value
                    else:
                        # Se não encontrar, manter referência original e logar warning
                        logger.warning(f"Variável de ambiente '{var_name}' não encontrada")
                        return match.group(0)  # Manter string original
                
                # Substituir todas as ocorrências
                resolved_value = re.sub(pattern, replace_env_var, value)
                resolved_config[key] = resolved_value
                
            elif isinstance(value, dict):
                # Recursivamente resolver dicionários aninhados
                resolved_config[key] = self._resolve_env_variables(value)
            else:
                # Manter outros tipos de dados como estão
                resolved_config[key] = value
        
        return resolved_config
    
    def create_crew_for_group(self, group_id: str) -> AdvancedInstagramPostCrew:
        """
        Cria uma instância de CrewAI para um grupo específico
        
        Args:
            group_id: ID do grupo para buscar a configuração
            
        Returns:
            AdvancedInstagramPostCrew: Instância configurada para o grupo
        """
        group_config = self._group_configs.get(group_id)
        
        if not group_config:
            logger.warning(f"⚠️  Configuração para grupo {group_id} não encontrada. Usando configuração padrão.")
            return AdvancedInstagramPostCrew()
        
        # Verificar se o grupo está ativo
        if not group_config.get('active', True):
            logger.warning(f"⚠️  Grupo {group_id} está inativo. Usando configuração padrão.")
            return AdvancedInstagramPostCrew()
        
        logger.info(f"✅ Criando CrewAI personalizado para grupo: {group_config.get('group_name', group_id)}")
        
        # Log do perfil sendo usado
        if 'crewai_agent_profile' in group_config:
            profile = group_config['crewai_agent_profile']
            logger.info(f"📝 Perfil do agente: {profile.get('profile_name', 'N/A')}")
            logger.info(f"🎭 Voz da marca: {profile.get('brand_voice', 'N/A')}")
            logger.info(f"🎨 Estilo: {profile.get('content_style', 'N/A')}")
        
        return AdvancedInstagramPostCrew(group_config)
    
    def get_available_groups(self) -> Dict[str, str]:
        """
        Retorna lista de grupos disponíveis
        
        Returns:
            Dict[str, str]: Dicionário com group_id -> group_name
        """
        return {
            group_id: config.get('group_name', group_id)
            for group_id, config in self._group_configs.items()
            if config.get('active', True)
        }
    
    def get_group_config(self, group_id: str) -> Optional[Dict[str, Any]]:
        """
        Retorna a configuração completa de um grupo
        
        Args:
            group_id: ID do grupo
            
        Returns:
            Optional[Dict[str, Any]]: Configuração do grupo ou None se não encontrado
        """
        return self._group_configs.get(group_id)
    
    def refresh_configs(self):
        """Recarrega as configurações dos grupos"""
        self._group_configs = self._load_group_configs()
        logger.info("🔄 Configurações recarregadas")


# Instância global do factory para uso em todo o sistema
crew_factory = CrewFactory()


def get_crew_for_group(group_id: str) -> AdvancedInstagramPostCrew:
    """
    Função utilitária para obter uma instância de CrewAI para um grupo
    
    Args:
        group_id: ID do grupo
        
    Returns:
        AdvancedInstagramPostCrew: Instância configurada
    """
    return crew_factory.create_crew_for_group(group_id)


def get_available_groups() -> Dict[str, str]:
    """
    Função utilitária para obter grupos disponíveis
    
    Returns:
        Dict[str, str]: Dicionário com group_id -> group_name
    """
    return crew_factory.get_available_groups()


def refresh_group_configs():
    """Função utilitária para recarregar configurações"""
    crew_factory.refresh_configs()


# Exemplo de uso
if __name__ == "__main__":
    logger.info("🧪 TESTE DO CREW FACTORY")
    
    # Listar grupos disponíveis
    logger.info("\n📋 Grupos disponíveis:")
    groups = get_available_groups()
    for group_id, name in groups.items():
        logger.info(f"  - {group_id}: {name}")
    
    # Testar criação para cada grupo
    for group_id in groups.keys():
        logger.info(f"\n🎯 Testando grupo: {group_id}")
        crew = get_crew_for_group(group_id)
        info = crew.get_profile_info()
        logger.info(f"  📝 Perfil: {info['profile_name']}")
        logger.info(f"  🎭 Voz: {info['brand_voice']}")
        logger.info(f"  🎨 Estilo: {info['content_style']}")
        logger.info(f"  👥 Público: {info['target_audience']}")