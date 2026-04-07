def final_node(state):
    state["final_output"] = {
        "summary": state["triage"],
        "logs": state["log_analysis"],
        "repro": state["repro_output"],
        "fix": state["fix_plan"],
        "critic": state["critic"]
    }
    print("✅ Final output ready")
    return state