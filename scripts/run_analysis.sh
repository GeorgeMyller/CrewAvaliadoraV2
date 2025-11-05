#!/bin/bash
# Quick script to run codebase analysis

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

if [ -z "$1" ]; then
    echo "❌ Usage: ./scripts/run_analysis.sh <github_url>"
    echo "Example: ./scripts/run_analysis.sh https://github.com/user/repo"
    exit 1
fi

echo "🚀 Running CrewAI Codebase Analysis"
echo "📦 Project: $1"
echo ""

python src/analyze_repo.py "$1"
