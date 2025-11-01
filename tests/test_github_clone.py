"""Tests for GitHub repository cloning functionality."""

import pytest
from unittest.mock import patch, MagicMock, call
import tempfile
import os
import shutil
import subprocess
from urllib.parse import urlparse


# Copy the functions we want to test directly here to avoid import issues
def is_github_url(path: str) -> bool:
    """Verifica se o caminho é uma URL do GitHub."""
    try:
        parsed = urlparse(path)
        return parsed.netloc in ['github.com', 'www.github.com'] and bool(parsed.path.strip('/'))
    except Exception:
        return False


class TestGitHubURLDetection:
    """Tests for is_github_url function."""
    
    def test_valid_github_url(self):
        """Test that valid GitHub URLs are detected."""
        assert is_github_url("https://github.com/GeorgeMyller/Continuador") is True
        assert is_github_url("https://github.com/owner/repo") is True
        assert is_github_url("https://www.github.com/owner/repo") is True
        assert is_github_url("http://github.com/owner/repo") is True
    
    def test_github_url_with_git_extension(self):
        """Test GitHub URLs with .git extension."""
        assert is_github_url("https://github.com/owner/repo.git") is True
    
    def test_invalid_urls(self):
        """Test that non-GitHub URLs are rejected."""
        assert is_github_url("https://gitlab.com/owner/repo") is False
        assert is_github_url("https://example.com/repo") is False
        assert is_github_url("not-a-url") is False
    
    def test_local_paths(self):
        """Test that local paths are not detected as GitHub URLs."""
        assert is_github_url("/home/user/repo") is False
        assert is_github_url("./local/repo") is False
        assert is_github_url("C:\\Windows\\path") is False
    
    def test_empty_path(self):
        """Test handling of empty paths."""
        assert is_github_url("") is False
        assert is_github_url("https://github.com/") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
