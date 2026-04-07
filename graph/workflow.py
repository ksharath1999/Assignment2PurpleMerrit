from langgraph.graph import StateGraph
from graph.state import AgentState

from agents.triage import triage_node
from agents.log_analysis import log_node
from agents.repro import repro_node
from agents.fix import fix_node
from agents.critic import critic_node
from agents.final import final_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("triage", triage_node)
    graph.add_node("log", log_node)
    graph.add_node("repro", repro_node)
    graph.add_node("fix", fix_node)
    graph.add_node("critic", critic_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("triage")

    graph.add_edge("triage", "log")
    graph.add_edge("log", "repro")
    graph.add_edge("repro", "fix")
    graph.add_edge("fix", "critic")
    graph.add_edge("critic", "final")

    return graph.compile()