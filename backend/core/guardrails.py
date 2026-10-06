import re
from typing import List, Tuple

class SecurityGuardrails:
    def __init__(self):
        self.injection_patterns: List[str] = [
            r"ignore previous instructions",
            r"system prompt",
            r"reveal your secrets",
            r"bypass guardrails",
            r"disregard all rules"
        ]
        self.pii_patterns: List[str] = [
            r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b",
            r"\b\d{10}\b"
        ]

    def validate_input(self, user_input: str) -> Tuple[bool, str]:
        """Validates user input against prompt injection attempts."""
        clean_input = user_input.lower()
        for pattern in self.injection_patterns:
            if re.search(pattern, clean_input):
                return False, f"Security Violation: Potential prompt injection detected ({pattern})."
        return True, "Input is safe."

    def validate_output(self, output_text: str) -> str:
        """Redacts sensitive PII information from agent outputs."""
        sanitized_text = output_text
        for pattern in self.pii_patterns:
            sanitized_text = re.sub(pattern, "[REDACTED_PII]", sanitized_text)
        return sanitized_text