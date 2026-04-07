from tools.log_parser import extract_errors

def log_node(state):
    state["log_analysis"] = {
        "errors": extract_errors(state["logs"])
    }
    print("✅ Log analysis done")
    return state