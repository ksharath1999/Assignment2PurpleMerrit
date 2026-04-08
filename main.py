import json
from graph.workflow import build_graph


def load_data():
    """Load input data (bug report + logs)"""
    with open("data/bug_report.json") as f:
        bug = json.load(f)

    with open("data/logs.txt") as f:
        logs = f.read()

    return {
        "bug_report": bug,
        "logs": logs,
        "retry_count": 0
    }


def save_output(result):
    """Save structured output to JSON file"""
    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)


if __name__ == "__main__":
    print("🚀 Starting Multi-Agent Debugging System...\n")

    # Build LangGraph workflow
    app = build_graph()

    # Load inputs
    state = load_data()

    # Run system
    result = app.invoke(state)

    # Extract final output
    final_output = result["final_output"]

    # Save output file (IMPORTANT for assignment)
    save_output(final_output)

    # Display output
    print("\n🔥 FINAL OUTPUT:\n")
    print(json.dumps(final_output, indent=4))

    print("\n📁 Output saved to: output.json")
    print("\n✅ Execution completed successfully!")
