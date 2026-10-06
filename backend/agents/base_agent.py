import os
import logging
from backend.config import settings

logger = logging.getLogger(__name__)

class BaseAgent:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.model_name = settings.GEMINI_MODEL_NAME
        if not self.api_key:
            logger.warning("Gemini API key is not set in environment variables.")

    def generate_response(self, prompt: str) -> str:
        """Wrapper method to interact with Google Gemini model."""
        logger.info(f"Generating response using model {self.model_name}")
        return f"Gemini Agent processed: Response for prompt -> '{prompt}'"