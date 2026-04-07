import json
from graph.workflow import build_graph

def load_data():
    with open("data/bug_report.json") as f:
        bug = json.load(f)

    with open("data/logs.txt") as f:
        logs = f.read()

    return {
        "bug_report": bug,
        "logs": logs,
        "retry_count": 0
    }

if __name__ == "__main__":
    app = build_graph()
    state = load_data()

    result = app.invoke(state)

    print("\n🔥 FINAL OUTPUT:\n")
    print(json.dumps(result["final_output"], indent=4))