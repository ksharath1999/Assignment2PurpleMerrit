# NOTE:
# This decision engine is designed to be replaceable with an LLM.
# Currently using heuristic fallback for offline execution.

def decision_node(state):
    logs = str(state.get("log_analysis", "")).lower()
    repro = str(state.get("repro_output", "")).lower()

    if "zerodivisionerror" in logs or "zerodivisionerror" in repro:
        decision = "bug_confirmed"
    elif "error" in repro or "exception" in repro:
        decision = "bug_confirmed"
    else:
        decision = "no_bug"

    state["decision"] = decision

    print(f"🧠 Decision Engine: {decision}")
    return state