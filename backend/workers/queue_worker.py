import logging
from backend.core.engine import ProductionAgentEngine
from backend.core.gateway import ToolGateway
from backend.core.guardrails import SecurityGuardrails
from backend.tools.registry import BusinessTools

logger = logging.getLogger(__name__)

class BackgroundQueueWorker:
    def __init__(self):
        self.guardrails = SecurityGuardrails()
        self.gateway = ToolGateway()
        self.gateway.register_tool("vector_search", BusinessTools.vector_search, "READ")
        self.gateway.register_tool("database_lookup", BusinessTools.database_lookup, "READ")
        self.gateway.register_tool("external_api_call", BusinessTools.external_api_call, "WRITE")
        
        self.engine = ProductionAgentEngine(tool_gateway=self.gateway, guardrails=self.guardrails)

    def process_background_goal(self, goal: str):
        logger.info(f"Background worker starting execution for goal: {goal}")
        result = self.engine.run_agent_loop(user_goal=goal)
        logger.info(f"Background worker finished goal. Result: {result}")
        return result