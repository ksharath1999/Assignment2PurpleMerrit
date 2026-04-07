def fix_node(state):
    errors = state["log_analysis"]["errors"]

    if any("ZeroDivisionError" in e for e in errors):
        root_cause = "Division by zero due to missing validation"
    else:
        root_cause = "Unknown issue"

    state["fix_plan"] = {
        "root_cause": root_cause,
        "patch": "if amount == 0: return 0",
        "risk": "May hide invalid input",
        "improvement": "Add proper validation and logging"
    }

    print("✅ Fix created")
    return state