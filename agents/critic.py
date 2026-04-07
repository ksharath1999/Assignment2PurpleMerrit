def critic_node(state):
    state["critic"] = {
        "issue": "no input validation",
        "suggestion": "add validation before division"
    }
    print("✅ Critic review done")
    return state