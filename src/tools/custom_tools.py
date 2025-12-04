import os
import shutil
import subprocess  # nosec

from crewai.tools import BaseTool
from pydantic import Field


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
            ruff_path = shutil.which("ruff")
            if not ruff_path:
                return "Error: 'ruff' is not installed in the environment."

            result = subprocess.run(
                [ruff_path, "check", "."],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=60,
            )  # nosec

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
            pip_audit_path = shutil.which("pip-audit")
            safety_path = shutil.which("safety")
            pip_path = shutil.which("pip")

            if pip_audit_path:
                cmd = [pip_audit_path, "."]
            # Fallback to safety if available
            elif safety_path:
                cmd = [safety_path, "check"]
            elif pip_path:
                # Fallback to pip list --outdated
                cmd = [pip_path, "list", "--outdated"]
                return (
                    "Warning: Neither 'pip-audit' nor 'safety' found. Running 'pip list --outdated' instead.\n"
                    + subprocess.run(cmd, cwd=self.repo_path, capture_output=True, text=True).stdout  # nosec
                )
            else:
                return "Error: No dependency checking tool found (pip-audit, safety, or pip)."

            result = subprocess.run(
                cmd, cwd=self.repo_path, capture_output=True, text=True, timeout=60
            )  # nosec
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
            pytest_path = shutil.which("pytest")
            if not pytest_path:
                return "Error: 'pytest' is not installed in the environment."

            result = subprocess.run(
                [pytest_path], cwd=self.repo_path, capture_output=True, text=True, timeout=120
            )  # nosec

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
            git_path = shutil.which("git")
            grep_path = shutil.which("grep")

            if os.path.exists(os.path.join(self.repo_path, ".git")) and git_path:
                cmd = [git_path, "grep", "-n", search_pattern]
            elif grep_path:
                cmd = [grep_path, "-r", "-n", search_pattern, "."]
            else:
                return "Error: Neither 'git' nor 'grep' found in the environment."

            result = subprocess.run(
                cmd, cwd=self.repo_path, capture_output=True, text=True, timeout=60
            )  # nosec

            output = f"Grep Output:\n{result.stdout}\n{result.stderr}"
            if len(output) > 5000:
                return output[:5000] + "\n... (output truncated)"
            return output
        except Exception as e:
            return f"Error running grep: {e}"
