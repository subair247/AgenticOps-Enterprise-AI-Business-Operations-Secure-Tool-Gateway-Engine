import logging
from typing import Dict, Any, Callable

logger = logging.getLogger(__name__)

class ToolGateway:
    def __init__(self):
        self.registered_tools: Dict[str, Dict[str, Any]] = {}

    def register_tool(self, name: str, func: Callable, permission_level: str):
        """Registers a tool with a specific permission level (READ, WRITE, EXECUTE)."""
        self.registered_tools[name] = {
            "function": func,
            "permission": permission_level
        }
        logger.info(f"Tool registered: {name} with permission {permission_level}")

    def execute_securely(self, tool_name: str, args: Dict[str, Any], caller_role: str = "standard_agent") -> str:
        """Enforces least-privilege security before running any tool."""
        if tool_name not in self.registered_tools:
            return f"Error: Tool '{tool_name}' is not registered in the Gateway."

        tool_info = self.registered_tools[tool_name]
        
        if tool_info["permission"] == "WRITE" and caller_role == "restricted_agent":
            logger.warning(f"Security Violation: Role '{caller_role}' attempted to execute WRITE tool '{tool_name}'.")
            return f"Security Violation: Role '{caller_role}' is not authorized to execute WRITE tool '{tool_name}'."

        try:
            logger.info(f"Executing tool '{tool_name}' with args: {args}")
            result = tool_info["function"](**args)
            return str(result)
        except Exception as e:
            logger.error(f"Error executing tool {tool_name}: {str(e)}")
            return f"Error executing tool {tool_name}: {str(e)}"