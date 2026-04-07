from memory import save_memory

def final_node(state):
    result = {
        "summary": state.get("triage"),
        "logs": state.get("log_analysis"),
        "repro": state.get("repro_output"),
        "decision": state.get("decision"),
        "fix": state.get("fix_plan"),
        "critic": state.get("critic"),
        "confidence": 0.9 if state.get("decision") == "bug_confirmed" else 0.5
    }

    state["final_output"] = result

    save_memory(result)

    print("💾 Memory saved")
    print("✅ Final output ready")

    return state