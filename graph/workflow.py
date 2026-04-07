from langgraph.graph import StateGraph
from graph.state import AgentState

from agents.triage import triage_node
from agents.log_analysis import log_node
from agents.repro import repro_node
from agents.decision import decision_node
from agents.fix import fix_node
from agents.critic import critic_node
from agents.final import final_node

MAX_RETRIES = 2

def retry_or_decide(state):
    if not state["repro_success"]:
        if state.get("retry_count", 0) < MAX_RETRIES:
            state["retry_count"] = state.get("retry_count", 0) + 1
            print("🔄 Retrying repro...")
            return "repro"
    return "decision"

def route_decision(state):
    return state["decision"]

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("triage", triage_node)
    graph.add_node("log", log_node)
    graph.add_node("repro", repro_node)
    graph.add_node("decision", decision_node)
    graph.add_node("fix", fix_node)
    graph.add_node("critic", critic_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("triage")

    graph.add_edge("triage", "log")
    graph.add_edge("log", "repro")

    # 🔥 Retry logic
    graph.add_conditional_edges(
        "repro",
        retry_or_decide,
        {
            "repro": "repro",
            "decision": "decision"
        }
    )

    # 🔥 Decision routing
    graph.add_conditional_edges(
        "decision",
        route_decision,
        {
            "bug_confirmed": "fix",
            "no_bug": "final"
        }
    )

    graph.add_edge("fix", "critic")
    graph.add_edge("critic", "final")

    return graph.compile()