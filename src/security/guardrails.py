import logging
import re
from typing import Optional

# Configure logging
logger = logging.getLogger(__name__)

class InputGuard:
    """
    🛡️ Guardrails for User Input Validation
    
    Protects the system from prompt injection and malicious inputs.
    Uses pattern matching and heuristics to detect potential attacks.
    """
    
    # Common prompt injection patterns
    INJECTION_PATTERNS = [
        r"ignore previous instructions",
        r"ignore all previous instructions",
        r"forget all previous instructions",
        r"system override",
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
        self.patterns = [re.compile(p, re.IGNORECASE) for p in self.INJECTION_PATTERNS]
        logger.info("🛡️ InputGuard initialized with basic injection patterns")

    def validate_prompt(self, prompt: str) -> tuple[bool, Optional[str]]:
        """
        Validates a user prompt against known injection patterns.
        
        Args:
            prompt: The user input string to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not prompt:
            return False, "Input cannot be empty"
            
        # Check length
        if len(prompt) > 10000:
            return False, "Input too long (max 10000 chars)"
            
        # Check against patterns
        for pattern in self.patterns:
            if pattern.search(prompt):
                logger.warning(f"⚠️ Potential prompt injection detected: {pattern.pattern}")
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
