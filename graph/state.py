from typing import TypedDict, Optional

class AgentState(TypedDict):
    bug_report: dict
    logs: str

    triage: dict
    log_analysis: dict

    repro_output: str
    repro_success: bool

    fix_plan: dict
    critic: dict

    decision: Optional[str]  # NEW
    final_output: dict