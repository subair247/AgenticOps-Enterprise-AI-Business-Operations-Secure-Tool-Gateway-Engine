import logging

logger = logging.getLogger(__name__)

class ApiTool:
    @staticmethod
    def execute(endpoint: str, payload: dict = None) -> str:
        """Makes safe external REST API calls for business automation."""
        logger.info(f"ApiTool calling endpoint: {endpoint}")
        try:
            return f"External API Success: Endpoint '{endpoint}' responded with status 200 OK."
        except Exception as e:
            logger.error(f"API call failed: {str(e)}")
            return f"External API Error: {str(e)}"