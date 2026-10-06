from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.engine import ProductionAgentEngine
from backend.core.gateway import ToolGateway
from backend.core.guardrails import SecurityGuardrails
from backend.tools.registry import BusinessTools

router = APIRouter()

class AgentRequest(BaseModel):
    goal: str
    role: str = "standard_agent"

@router.run_agent if hasattr(router, 'run_agent') else router.post("/run")
def run_agent_task(payload: AgentRequest):
    try:
        guardrails = SecurityGuardrails()
        gateway = ToolGateway()
        gateway.register_tool("vector_search", BusinessTools.vector_search, "READ")
        gateway.register_tool("database_lookup", BusinessTools.database_lookup, "READ")
        gateway.register_tool("external_api_call", BusinessTools.external_api_call, "WRITE")
        
        engine = ProductionAgentEngine(tool_gateway=gateway, guardrails=guardrails)
        result = engine.run_agent_loop(user_goal=payload.goal, caller_role=payload.role)
        
        return {"status": "success", "goal": payload.goal, "output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))