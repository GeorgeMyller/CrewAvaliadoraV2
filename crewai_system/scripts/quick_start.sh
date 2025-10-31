#!/bin/bash

# 🚀 CrewAI System - Quick Start Script
# Executa o sistema de análise de codebase com 6 agentes especializados

echo "🚀 CrewAI System - Análise Automatizada de Codebase"
echo "=================================================="
echo ""

# Verificar se estamos na pasta correta
if [[ ! -f "crew_gemini_simples.py" ]]; then
    echo "❌ Erro: Execute este script na pasta crewai_system/scripts/"
    echo "💡 Solução: cd crewai_system/scripts && ./quick_start.sh"
    exit 1
fi

# Verificar se a API key está configurada
if [[ -z "$GEMINI_API_KEY" ]]; then
    echo "❌ Erro: GEMINI_API_KEY não configurada"
    echo "💡 Solução: export GEMINI_API_KEY='sua_api_key_aqui'"
    exit 1
fi

echo "✅ Configuração OK - Iniciando análise..."
echo ""

# Executar verificação de saúde primeiro
echo "🔍 1. Verificando saúde do sistema..."
uv run crew_health_check.py

if [[ $? -eq 0 ]]; then
    echo "✅ Sistema saudável - Prosseguindo com análise completa"
    echo ""
    
    # Executar análise completa
    echo "🤖 2. Iniciando análise com 6 agentes especializados..."
    echo "   🏗️  Arquiteto de Software"
    echo "   🧪 Engenheiro de Qualidade"
    echo "   📄 Documentador Técnico"
    echo "   🚀 Product Manager"
    echo "   ⚖️  Especialista Legal"
    echo "   🤖 Engenheiro de IA"
    echo ""
    echo "⏱️  Tempo estimado: 8-12 minutos"
    echo "💰 Custo estimado: $0.15-0.25 USD"
    echo ""
    
    uv run crew_gemini_simples.py
    
    if [[ $? -eq 0 ]]; then
        echo ""
        echo "🎉 Análise concluída com sucesso!"
        echo "📄 Verifique o relatório gerado na pasta ../reports/"
        echo ""
        echo "📊 Relatório contém:"
        echo "   ✅ Executive Summary"
        echo "   ✅ Score de Maturidade (0-100)"
        echo "   ✅ Análise de 6 especialistas"
        echo "   ✅ Roadmap estratégico"
        echo "   ✅ Top 5 riscos críticos"
        echo "   ✅ Quick wins"
    else
        echo "❌ Erro durante a análise"
        echo "💡 Tente executar novamente: uv run crew_gemini_simples.py"
    fi
else
    echo "⚠️  Sistema com problemas - Executando análise mesmo assim..."
    uv run crew_gemini_simples.py
fi

echo ""
echo "🔗 Para mais opções, consulte: ../README.md"
