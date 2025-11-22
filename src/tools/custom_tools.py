from crewai.tools import BaseTool
from pydantic import Field, PrivateAttr
import subprocess
import os
import shutil

class RunLinterTool(BaseTool):
    name: str = "Run Linter"
    description: str = "Executes ruff linter on the codebase to find quality issues. Returns the output of the linter."
    repo_path: str = Field(..., description="Path to the repository to analyze")

    def _run(self, argument: str = None) -> str:
        """
        Executes ruff linter on the repository.
        The 'argument' parameter is ignored as we run on the whole repo.
        """
        if not os.path.exists(self.repo_path):
            return f"Error: Repository path {self.repo_path} does not exist."

        try:
            # Check if ruff is installed
            if not shutil.which("ruff"):
                return "Error: 'ruff' is not installed in the environment."

            result = subprocess.run(
                ["ruff", "check", "."],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            output = f"Ruff Linter Output:\n{result.stdout}\n{result.stderr}"
            if len(output) > 5000:
                return output[:5000] + "\n... (output truncated)"
            return output
        except Exception as e:
            return f"Error running linter: {e}"

class CheckDependenciesTool(BaseTool):
    name: str = "Check Dependencies"
    description: str = "Checks dependencies for known vulnerabilities using safety or pip-audit. Returns the security report."
    repo_path: str = Field(..., description="Path to the repository to analyze")

    def _run(self, argument: str = None) -> str:
        """
        Checks dependencies for vulnerabilities.
        """
        if not os.path.exists(self.repo_path):
            return f"Error: Repository path {self.repo_path} does not exist."

        try:
            # Try pip-audit first
            if shutil.which("pip-audit"):
                cmd = ["pip-audit", "."]
            # Fallback to safety if available
            elif shutil.which("safety"):
                cmd = ["safety", "check"]
            else:
                # Fallback to pip list --outdated
                cmd = ["pip", "list", "--outdated"]
                return "Warning: Neither 'pip-audit' nor 'safety' found. Running 'pip list --outdated' instead.\n" + \
                       subprocess.run(cmd, cwd=self.repo_path, capture_output=True, text=True).stdout

            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            return f"Dependency Check Output ({cmd[0]}):\n{result.stdout}\n{result.stderr}"
        except Exception as e:
            return f"Error checking dependencies: {e}"

class ExecuteTestsTool(BaseTool):
    name: str = "Execute Tests"
    description: str = "Executes the project's test suite using pytest. Returns the test results."
    repo_path: str = Field(..., description="Path to the repository to analyze")

    def _run(self, argument: str = None) -> str:
        """
        Executes tests using pytest.
        """
        if not os.path.exists(self.repo_path):
            return f"Error: Repository path {self.repo_path} does not exist."

        try:
            # Check if pytest is installed
            if not shutil.which("pytest"):
                return "Error: 'pytest' is not installed in the environment."

            result = subprocess.run(
                ["pytest"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            output = f"Test Execution Output:\n{result.stdout}\n{result.stderr}"
            if len(output) > 5000:
                return output[:5000] + "\n... (output truncated)"
            return output
        except Exception as e:
            return f"Error running tests: {e}"

class GrepTool(BaseTool):
    name: str = "Grep Search"
    description: str = "Search for a string or pattern in the codebase using grep. Returns matching lines with line numbers."
    repo_path: str = Field(..., description="Path to the repository to search in")

    def _run(self, search_pattern: str) -> str:
        """
        Executes grep on the repository.
        """
        if not os.path.exists(self.repo_path):
            return f"Error: Repository path {self.repo_path} does not exist."

        try:
            # Use git grep if it's a git repo, otherwise regular grep
            if os.path.exists(os.path.join(self.repo_path, ".git")):
                cmd = ["git", "grep", "-n", search_pattern]
            else:
                cmd = ["grep", "-r", "-n", search_pattern, "."]

            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            output = f"Grep Output:\n{result.stdout}\n{result.stderr}"
            if len(output) > 5000:
                return output[:5000] + "\n... (output truncated)"
            return output
        except Exception as e:
            return f"Error running grep: {e}"
