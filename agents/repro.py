from tools.repro_runner import run_test

def repro_node(state):
    code = """
def test():
    x = 100 / 0

test()
"""
    with open("test_bug.py", "w") as f:
        f.write(code)

    state["repro_output"] = run_test("test_bug.py")

    print("✅ Repro done")
    return state