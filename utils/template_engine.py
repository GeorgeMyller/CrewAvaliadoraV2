"""
📄 Template Engine - Processador de Templates com Placeholders
================================================================

Processa templates markdown substituindo placeholders por valores reais.
"""

import re
from typing import Dict, Any, Optional
from pathlib import Path
from datetime import datetime


class TemplateEngine:
    """Engine para processar templates com substituição de placeholders"""
    
    def __init__(self, template_path: Optional[str] = None):
        """
        Inicializa engine com template.
        
        Args:
            template_path: Caminho para o template markdown
        """
        if template_path is None:
            template_path = "templates/template_relatorio_final_v2.md"
        
        self.template_path = template_path
        self.template_content = self._load_template()
    
    def _load_template(self) -> str:
        """Carrega template do arquivo"""
        try:
            with open(self.template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template não encontrado: {self.template_path}")
    
    def render(self, context: Dict[str, Any]) -> str:
        """
        Renderiza template substituindo placeholders.
        
        Args:
            context: Dicionário com valores para substituir
            
        Returns:
            Template renderizado
        """
        result = self.template_content
        
        # Substitui placeholders {{key}}
        for key, value in context.items():
            placeholder = f"{{{{{key}}}}}"
            result = result.replace(placeholder, str(value))
        
        return result
    
    def extract_placeholders(self) -> list:
        """
        Extrai todos os placeholders do template.
        
        Returns:
            Lista de placeholders encontrados
        """
        pattern = r'\{\{(\w+)\}\}'
        matches = re.findall(pattern, self.template_content)
        return list(set(matches))
    
    def validate_context(self, context: Dict[str, Any]):
        """
        Valida se todos os placeholders têm valores.
        
        Args:
            context: Dicionário com valores
            
        Returns:
            Tupla (is_valid, missing_keys)
        """
        required = set(self.extract_placeholders())
        provided = set(context.keys())
        missing = required - provided
        
        return (len(missing) == 0, list(missing))


def calculate_scores(analysis_results: Dict[str, str]) -> Dict[str, int]:
    """
    Calcula scores baseado nos resultados das análises.
    
    Args:
        analysis_results: Dicionário com resultados de cada agente
        
    Returns:
        Dicionário com scores calculados
    """
    scores = {}
    
    # Tenta extrair scores das análises
    score_pattern = r'[Ss]core[:\s]+(\d+)'
    
    for key, content in analysis_results.items():
        matches = re.findall(score_pattern, str(content))
        if matches:
            scores[f"{key}_score"] = int(matches[0])
        else:
            scores[f"{key}_score"] = 70
    
    # Calcula score geral
    if scores:
        overall = sum(scores.values()) // len(scores)
        scores['overall_score'] = overall
    else:
        scores['overall_score'] = 70
    
    return scores


def create_report_context(
    analysis_results: Dict[str, str],
    project_name: str = "Project",
    workspace_path: str = "."
) -> Dict[str, Any]:
    """
    Cria contexto completo para renderização do relatório.
    """
    scores = calculate_scores(analysis_results)
    
    context = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'project_name': project_name,
        'workspace_path': workspace_path,
        'test_coverage': 0,
        **scores,
        **analysis_results,
    }
    
    return context


def render_report(
    analysis_results: Dict[str, str],
    template_path: Optional[str] = None,
    project_name: str = "Project",
    workspace_path: str = "."
) -> str:
    """Helper function para renderizar relatório completo."""
    engine = TemplateEngine(template_path)
    context = create_report_context(analysis_results, project_name, workspace_path)
    
    # Valida e adiciona valores padrão
    is_valid, missing = engine.validate_context(context)
    if not is_valid:
        for key in missing:
            context[key] = f"[{key} não disponível]"
    
    return engine.render(context)


if __name__ == "__main__":
    try:
        engine = TemplateEngine()
        print("✅ Template carregado!")
        
        placeholders = engine.extract_placeholders()
        print(f"📋 {len(placeholders)} placeholders encontrados")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
