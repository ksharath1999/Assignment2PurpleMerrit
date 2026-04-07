def final_node(state):
    result = {
        "bug_summary": state.get("triage"),
        "evidence": state.get("log_analysis"),
        "repro_steps": "Run: python test_bug.py",
        "repro_artifact": "test_bug.py",
        "repro_output": state.get("repro_output"),
        "root_cause": state.get("fix_plan", {}).get("root_cause"),
        "patch_plan": state.get("fix_plan"),
        "validation_plan": "Add unit tests for zero and negative inputs",
        "open_questions": "Should zero transactions be allowed?",
        "critic": state.get("critic"),
        "confidence": 0.9 if state.get("decision") == "bug_confirmed" else 0.5
    }

    state["final_output"] = result

    from memory import save_memory
    save_memory(result)

    print("💾 Memory saved")
    print("✅ Final output ready")

    return state