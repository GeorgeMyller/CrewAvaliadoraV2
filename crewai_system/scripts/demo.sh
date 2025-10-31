#!/bin/bash

# 🎯 Demo Rápido - CrewAI System
# Executa apenas um teste básico para demonstrar o funcionamento

echo "🎯 CrewAI System - Demo Rápido"
echo "==============================="
echo ""
echo "Este demo executa uma verificação rápida do sistema."
echo "Para análise completa, use: ./quick_start.sh"
echo ""

# Verificar se estamos na pasta correta
if [[ ! -f "crew_health_check.py" ]]; then
    echo "❌ Execute na pasta crewai_system/scripts/"
    exit 1
fi

# Verificar API key
if [[ -z "$GEMINI_API_KEY" ]]; then
    echo "⚠️  GEMINI_API_KEY não configurada"
    echo "💡 Para demo completo, configure: export GEMINI_API_KEY='sua_key'"
    echo ""
    echo "🔍 Executando verificação offline..."
else
    echo "✅ API Key configurada - Executando verificação completa..."
fi

echo ""

# Executar health check
uv run crew_health_check.py

echo ""
echo "📖 Próximos passos:"
echo "   1. Configure GEMINI_API_KEY se ainda não configurou"
echo "   2. Execute: ./quick_start.sh para análise completa"
echo "   3. Consulte: ../README.md para documentação"
echo ""
echo "🎉 Demo concluído!"
