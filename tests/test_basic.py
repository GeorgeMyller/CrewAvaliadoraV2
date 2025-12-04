"""Basic tests to verify project setup."""

from pathlib import Path

import pytest


def test_project_structure():
    """Test that essential directories exist."""
    assert Path("outputs").exists()
    assert Path("outputs/reports").exists()
    assert Path("tests").exists()


def test_config_files():
    """Test that configuration files exist."""
    assert Path("pyproject.toml").exists()
    assert Path(".env.example").exists()
    assert Path(".gitignore").exists()


def test_main_scripts():
    """Test that main scripts exist."""
    assert Path("src/crew_avaliadora.py").exists()
    assert Path("src/analyze_repo.py").exists()
    assert Path("src/legacy/gerar_relatorio.py").exists()


def test_imports():
    """Test that key modules can be imported."""
    try:
        import crewai
        import google.generativeai as genai
        from dotenv import load_dotenv

        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import required module: {e}")
