def critic_node(state):
    issues = []

    if "validation" not in str(state["fix_plan"]).lower():
        issues.append("Fix lacks validation")

    if len(state["repro_output"]) < 20:
        issues.append("Repro is weak")

    state["critic"] = {
        "issues": issues,
        "verdict": "Needs improvement" if issues else "Looks good"
    }

    print("✅ Critic review done")
    return state