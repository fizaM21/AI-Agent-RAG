from typing import TypedDict


class AgentState(TypedDict):
    query: str
    resolved_query: str
    tool: str
    tool_input: str
    tool_result: str
    final_answer: str