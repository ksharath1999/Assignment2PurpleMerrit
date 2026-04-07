from tools.repro_runner import run_test

def repro_node(state):
    code = """
def process_payment(amount):
    return 100 / amount

print(process_payment(0))
"""

    with open("test_bug.py", "w") as f:
        f.write(code)

    output = run_test("test_bug.py")

    state["repro_output"] = output
    state["repro_success"] = "error" in output.lower() or "exception" in output.lower()

    print(f"🔁 Repro attempt {state.get('retry_count', 0)}")

    return state
