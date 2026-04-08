🚀 Multi-Agent Bug Reproduction & Fix System (LangGraph)
👨‍💻 Author

K Sharath
AI/ML Engineer Candidate

📌 Overview

This project implements a production-style multi-agent debugging system using LangGraph.

The system ingests a bug report and logs, reproduces the issue programmatically, analyzes failures, and generates a root-cause hypothesis, patch plan, and validation strategy.

It simulates a real-world engineering debugging workflow using coordinated agents.

🎯 Objective

To design a deterministic, tool-using multi-agent system that:

Parses bug reports and logs
Reproduces failures via executable scripts
Identifies root causes
Proposes safe fixes
Validates and critiques the solution
Produces structured, traceable output
🧠 Input Mode
✅ Option B (Log + Report Only)

This system uses Option B from the assignment:

No full repository required
Generates a minimal reproduction script dynamically
Provides patch plan at design level
📥 Inputs
1. Bug Report (data/bug_report.json)
{
  "title": "Division by zero error",
  "description": "Crash when processing zero amount",
  "expected_behavior": "Should handle safely",
  "actual_behavior": "Crash occurs when amount is 0",
  "environment": "Python 3.11, Windows",
  "repro_hints": "Occurs when amount is 0"
}
2. Logs (data/logs.txt)
INFO: Starting payment processing
ERROR: Exception occurred
Traceback (most recent call last):
  File "payment.py", line 10
    fee = 100 / amount
ZeroDivisionError: division by zero
WARNING: retry attempt
🧩 System Architecture
        ┌──────────────┐
        │   TRIAGE     │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ LOG ANALYSIS │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ REPRODUCTION │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   DECISION   │
        └──────┬───────┘
        ┌──────┴───────────┐
        ↓                  ↓
   (bug_confirmed)     (no_bug)
        ↓                  ↓
   ┌───────────┐        ┌────────┐
   │ FIX PLAN  │        │ FINAL  │
   └────┬──────┘        └────────┘
        ↓
   ┌───────────┐
   │  CRITIC   │
   └────┬──────┘
        ↓
     FINAL
🤖 Agent Roles
🔹 Triage Agent
Extracts symptoms and severity from bug report
Defines initial problem context
🔹 Log Analysis Agent
Parses logs
Extracts error signatures and stack traces
Filters relevant evidence
🔹 Reproduction Agent
Generates minimal failing script (test_bug.py)
Executes it programmatically
Captures runtime failure
🔹 Decision Agent
Determines whether bug is confirmed
Uses heuristic reasoning (LLM-replaceable design)
🔹 Fix Planner Agent
Identifies root cause
Proposes patch strategy
Highlights risks and improvements
🔹 Critic Agent
Validates fix safety
Checks edge cases
Flags weak assumptions
⚙️ Core Features
🔥 Multi-Agent Orchestration
Built using LangGraph
Stateful execution with shared data
Explicit agent handoffs
🔥 Conditional Workflow
Dynamic routing based on decision agent
Bug-confirmed vs no-bug paths
🔥 Retry Mechanism
Reproduction retries on failure
Improves robustness and reliability
🔥 Tool Usage
Log parsing tools
Script execution via subprocess
Log search/filtering
🔥 Minimal Reproducible Artifact
Auto-generated failing script
Consistent reproduction
🔥 Memory System
Stores past runs in memory.json
Enables future learning/analysis
🔥 Structured Output

Example output:

{
  "bug_summary": {...},
  "evidence": {...},
  "repro_steps": "Run: python test_bug.py",
  "repro_artifact": "test_bug.py",
  "root_cause": "...",
  "patch_plan": {...},
  "validation_plan": "...",
  "open_questions": "...",
  "confidence": 0.9
}
▶️ How to Run
pip install -r requirements.txt
python main.py
🧪 Reproduction Details

Generated file:

test_bug.py

Run manually:

python test_bug.py

Expected output:

ZeroDivisionError: division by zero
🧾 Traceability

The system logs execution steps:

Triage → Log Analysis → Reproduction → Decision → Fix → Critic → Final

Each agent prints its progress to console, ensuring full traceability.

📂 Project Structure
langgraph-bug-system/
│
├── agents/        # Agent implementations
├── tools/         # Utility tools
├── graph/         # LangGraph workflow
├── data/          # Input files
├── memory.py      # Persistent storage
├── main.py        # Entry point
├── requirements.txt
🧠 Design Highlights
Modular agent architecture
Deterministic workflow design
Pluggable decision engine (LLM-ready)
Separation of logic and orchestration
Focus on reproducibility and reliability
🚀 Future Improvements
Integrate LLM for reasoning (OpenAI/Claude)
Add RAG-based log intelligence
Support large-scale log processing
Add evaluation pipelines
Dockerize for deployment
🎯 Key Takeaways

This project demonstrates:

✔ Multi-agent system design
✔ Graph-based orchestration
✔ Debugging automation
✔ Tool-driven execution
✔ Production-oriented architecture

🎥 Demo

A short demo video showing system execution and output generation is included in submission.

📌 Final Note

This system is designed to mimic real-world debugging workflows, combining:

agent-based reasoning
execution-based validation
structured decision-making