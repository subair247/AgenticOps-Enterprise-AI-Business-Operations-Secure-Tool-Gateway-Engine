import logging
from typing import TypedDict, List
from langgraph.graph import StateGraph, END

logger = logging.getLogger(__name__)

class AgentGraphState(TypedDict):
    goal: str
    messages: List[str]
    plan: str
    observation: str
    is_complete: bool

class MultiAgentWorkflow:
    def __init__(self):
        self.workflow = StateGraph(AgentGraphState)
        self._build_graph()

    def _planner_node(self, state: AgentGraphState):
        logger.info("Multi-Agent Graph: Planner node executing...")
        state["plan"] = f"Break down goal: {state['goal']} into actionable steps."
        state["messages"].append("Planner created execution plan.")
        return state

    def _executor_node(self, state: AgentGraphState):
        logger.info("Multi-Agent Graph: Executor node executing...")
        state["observation"] = "Executed tools successfully across secure gateway."
        state["messages"].append("Executor retrieved required data.")
        state["is_complete"] = True
        return state

    def _build_graph(self):
        self.workflow.add_node("planner", self._planner_node)
        self.workflow.add_node("executor", self._executor_node)

        self.workflow.set_entry_point("planner")
        self.workflow.add_edge("planner", "executor")
        self.workflow.add_edge("executor", END)

        self.app = self.workflow.compile()

    def run_workflow(self, user_goal: str):
        initial_state = {
            "goal": user_goal,
            "messages": [],
            "plan": "",
            "observation": "",
            "is_complete": False
        }
        return self.app.invoke(initial_state)