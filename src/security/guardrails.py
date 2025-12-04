import logging
import re

# Configure logging
logger = logging.getLogger(__name__)


class InputGuard:
    """
    🛡️ Guardrails for User Input Validation

    Protects the system from prompt injection and malicious inputs.
    Uses pattern matching and heuristics to detect potential attacks.
    """

    # Patterns that indicate an attempt to override system instructions
    PROMPT_INJECTION_PATTERNS = [
        r"ignore previous instructions",
        r"ignore all previous instructions",
        r"forget all previous instructions",
        r"system override",
    ]

    # Patterns that look like dangerous code execution
    # These might be valid in a codebase analysis context, so we can disable checking them
    DANGEROUS_CODE_PATTERNS = [
        r"delete all files",
        r"rm -rf",
        r"drop table",
        r"exec\s*\(",
        r"eval\s*\(",
        r"import\s+os",
        r"import\s+sys",
        r"sudo\s+",
    ]

    def __init__(self):
        self.prompt_patterns = [re.compile(p, re.IGNORECASE) for p in self.PROMPT_INJECTION_PATTERNS]
        self.code_patterns = [re.compile(p, re.IGNORECASE) for p in self.DANGEROUS_CODE_PATTERNS]
        logger.info("🛡️ InputGuard initialized with separated patterns")

    def validate_prompt(
        self, 
        prompt: str, 
        max_length: int = 10000,
        check_code_patterns: bool = True
    ) -> tuple[bool, str | None]:
        """
        Validates a user prompt against known injection patterns.

        Args:
            prompt: The user input string to validate
            max_length: Maximum allowed length for the input (default: 10000)
            check_code_patterns: Whether to check for dangerous code patterns (default: True)
                               Set to False when analyzing trusted codebases.

        Returns:
            tuple: (is_valid, error_message)
        """
        if not prompt:
            return False, "Input cannot be empty"

        # Check length
        if len(prompt) > max_length:
            return False, f"Input too long (max {max_length} chars)"

        # Check against prompt injection patterns (ALWAYS CHECKED)
        for pattern in self.prompt_patterns:
            if pattern.search(prompt):
                logger.warning(f"⚠️ Potential prompt injection detected: {pattern.pattern}")
                return False, "Potential security risk detected in input. Request blocked."

        # Check against dangerous code patterns (OPTIONAL)
        if check_code_patterns:
            for pattern in self.code_patterns:
                if pattern.search(prompt):
                    logger.warning(f"⚠️ Potential dangerous code detected: {pattern.pattern}")
                    return False, "Potential security risk detected in input. Request blocked."

        return True, None

    def sanitize_input(self, input_str: str) -> str:
        """
        Basic sanitization of input string.
        """
        if not input_str:
            return ""
        # Remove null bytes
        return input_str.replace("\0", "")
