import logging
from fastapi import FastAPI, Depends
from backend.config import settings
from backend.core.guardrails import SecurityGuardrails
from backend.core.gateway import ToolGateway
from backend.tools.registry import BusinessTools
from backend.core.engine import ProductionAgentEngine
from backend.api.v1.auth import verify_api_key
from backend.api.v1 import health, agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Enterprise-grade AI Business Operations Agent Platform with Loop & Harness Engineering."
)

guardrails = SecurityGuardrails()
gateway = ToolGateway()

gateway.register_tool("vector_search", BusinessTools.vector_search, "READ")
gateway.register_tool("database_lookup", BusinessTools.database_lookup, "READ")
gateway.register_tool("external_api_call", BusinessTools.external_api_call, "WRITE")

agent_engine = ProductionAgentEngine(tool_gateway=gateway, guardrails=guardrails)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["Health"])
app.include_router(
    agent.router, 
    prefix=settings.API_V1_STR, 
    tags=["Agent Operations"],
    dependencies=[Depends(verify_api_key)]
)

@app.get("/")
def root():
    return {
        "platform": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "Operational",
        "docs_url": "/docs"
    }