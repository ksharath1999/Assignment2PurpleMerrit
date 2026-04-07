🚀 Multi-Agent Bug Reproduction & Fix System (LangGraph)
📌 Overview

This project implements a production-style multi-agent debugging system using LangGraph.

The system ingests a bug report and logs, reproduces the issue, analyzes failures, and proposes a fix plan using coordinated agents.

It simulates how real engineering teams triage and resolve bugs—automated through an intelligent workflow.

🧠 Key Features
🔹 Multi-Agent Orchestration
Triage Agent → extracts bug context
Log Analysis Agent → parses and identifies errors
Reproduction Agent → generates and runs failing code
Decision Agent → determines if bug is confirmed
Fix Planner Agent → proposes root cause & patch
Critic Agent → validates and improves solution
🔹 LangGraph Workflow (Core Highlight)
Stateful graph-based execution
Conditional routing (dynamic decision paths)
Retry mechanism for robustness
Deterministic and explainable flow
🔹 Intelligent Decision Engine
Heuristic-based reasoning (LLM-replaceable design)
Designed for offline reliability
Can be extended with LLM APIs (OpenAI, Claude)
🔹 Automated Bug Reproduction
Generates minimal failing script
Executes via subprocess
Captures real runtime errors
🔹 Retry Mechanism
Automatically retries reproduction on failure
Prevents false negatives
Improves system reliability
🔹 Memory System
Stores past runs in memory.json
Enables future extension for learning/debug history
🔹 Structured Output

Produces final structured JSON:

{
  "summary": {...},
  "logs": {...},
  "repro": "...",
  "decision": "bug_confirmed",
  "fix": {...},
  "critic": {...},
  "confidence": 0.9
}
🏗️ Architecture
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
⚙️ Installation
pip install -r requirements.txt
▶️ Run the Project
python main.py
📂 Project Structure
langgraph-bug-system/
│
├── agents/        # Individual agent logic
├── tools/         # Utility tools (log parsing, execution)
├── graph/         # LangGraph workflow + state
├── data/          # Input data (bug report, logs)
├── memory.py      # Persistent memory
├── main.py        # Entry point
🧪 Example Workflow
Load bug report + logs
Analyze logs for error patterns
Generate minimal reproduction
Execute and capture failure
Decide if bug is confirmed
Generate fix plan
Critically evaluate solution
Store results in memory
🔍 Design Highlights
Pluggable decision engine (LLM-ready)
Deterministic fallback for reliability
Separation of orchestration and logic
Extensible agent-based architecture
🚀 Future Improvements
Integrate LLM (OpenAI / Claude) for reasoning
Add RAG for log intelligence
Introduce vector database for memory
Add evaluation pipelines (regression testing)
Dockerize for deployment
🎯 Why This Project

This project demonstrates:

✔ Multi-agent orchestration
✔ LangGraph workflow design
✔ Debugging system automation
✔ Tool integration & execution
✔ Production-style architecture

📌 Tech Stack
Python
LangGraph
Subprocess (execution engine)
JSON-based memory system
🧠 Author

[Your Name]
AI/ML Engineer Candidate

🎥 Demo

(Attach your screen recording here showing execution + output)

🔥 Final Note

This system is designed to simulate real-world debugging workflows, combining:

agent-based reasoning
execution-based validation
structured decision-making