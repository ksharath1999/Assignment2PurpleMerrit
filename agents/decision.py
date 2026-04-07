def decision_node(state):
    output = state["repro_output"]

    if "ZeroDivisionError" in output:
        state["decision"] = "bug_confirmed"
    else:
        state["decision"] = "no_bug"

    print(f"🧠 Decision: {state['decision']}")
    return state