from tools.search import search_logs

def log_node(state):
    errors = search_logs(state["logs"], "error")

    state["log_analysis"] = {
        "errors": errors
    }

    print("✅ Log analysis done")
    return state