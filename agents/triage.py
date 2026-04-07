def triage_node(state):
    state["triage"] = {
        "issue": state["bug_report"]["actual_behavior"],
        "priority": "high"
    }
    print("✅ Triage done")
    return state