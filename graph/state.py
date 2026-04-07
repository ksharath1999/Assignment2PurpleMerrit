from typing import TypedDict

class AgentState(TypedDict):
    bug_report: dict
    logs: str
    triage: dict
    log_analysis: dict
    repro_output: str
    fix_plan: dict
    critic: dict
    final_output: dict