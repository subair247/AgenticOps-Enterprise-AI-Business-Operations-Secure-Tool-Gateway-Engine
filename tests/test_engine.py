import pytest
from backend.core.engine import ProductionAgentEngine
from backend.core.gateway import ToolGateway
from backend.core.guardrails import SecurityGuardrails
from backend.tools.registry import BusinessTools

def test_agent_engine_run():
    gateway = ToolGateway()
    gateway.register_tool("vector_search", BusinessTools.vector_search, "READ")
    guardrails = SecurityGuardrails()
    
    engine = ProductionAgentEngine(tool_gateway=gateway, guardrails=guardrails, max_iterations=2)
    result = engine.run_agent_loop("Check Q4 sales target")
    assert "Goal achieved successfully" in result