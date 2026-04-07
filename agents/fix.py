def fix_node(state):
    state["fix_plan"] = {
        "cause": "division by zero",
        "fix": "if value == 0: handle safely"
    }
    print("✅ Fix created")
    return state