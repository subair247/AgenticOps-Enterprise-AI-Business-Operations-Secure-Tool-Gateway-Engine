from typing import Dict, Any

class ProductionAgentEngine:
    def __init__(self, tool_gateway: Any, guardrails: Any, max_iterations: int = 5):
        self.tool_gateway = tool_gateway
        self.guardrails = guardrails
        self.max_iterations = max_iterations

    def run_agent_loop(self, user_goal: str, caller_role: str = "standard_agent") -> str:
        is_safe, message = self.guardrails.validate_input(user_goal)
        if not is_safe:
            return f"Blocked: {message}"

        iteration = 0
        current_state = {"goal": user_goal, "status": "IN_PROGRESS"}

        while iteration < self.max_iterations:
            iteration += 1

            plan = self._generate_plan(current_state)

            observation = self.tool_gateway.execute_securely(
                tool_name=plan["tool"],
                args=plan["args"],
                caller_role=caller_role
            )

            is_complete, eval_note = self._check_goal_completion(current_state, observation)

            if is_complete:
                final_output = f"""### Executive Summary
{observation}"""
                return self.guardrails.validate_output(final_output)

            current_state["latest_observation"] = observation

        return "Agent stopped: Reached max iterations without finishing the goal."

    def _generate_plan(self, state: Dict[str, Any]) -> Dict[str, Any]:
        goal_lower = state["goal"].lower()
        if any(kw in goal_lower for kw in ["database", "employee", "server", "uptime", "count", "metrics", "records"]):
            return {"tool": "database_lookup", "args": {"query": state["goal"]}}
        elif any(kw in goal_lower for kw in ["api", "sync", "external", "endpoint"]):
            return {"tool": "external_api_call", "args": {"endpoint": "/v1/external-sync"}}
        else:
            return {"tool": "vector_search", "args": {"query": state["goal"]}}

    def _check_goal_completion(self, state: Dict[str, Any], observation: str) -> tuple[bool, str]:
        return True, "Information retrieved successfully."