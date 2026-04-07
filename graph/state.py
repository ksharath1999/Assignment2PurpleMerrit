from typing import TypedDict, Optional

class AgentState(TypedDict):
    bug_report: dict
    logs: str

    triage: dict
    log_analysis: dict

    repro_output: str
    repro_success: bool
    retry_count: int  # NEW

    decision: Optional[str]

    fix_plan: dict
    critic: dict

    final_output: dict