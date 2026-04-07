from llm import llm

def decision_node(state):
    prompt = f"""
You are an expert debugging system.

Logs:
{state['log_analysis']}

Reproduction Output:
{state['repro_output']}

Decide:
- bug_confirmed
- no_bug

Respond with ONLY one word.
"""

    response = llm.invoke(prompt)
    decision = response.content.strip().lower()

    if "bug" in decision:
        state["decision"] = "bug_confirmed"
    else:
        state["decision"] = "no_bug"

    print(f"🧠 LLM Decision: {state['decision']}")
    return state