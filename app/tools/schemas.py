from pydantic import BaseModel
from typing import Optional


class ToolRequest(BaseModel):
    tool_name: str
    query: str
    parameters: Optional[dict] = {}
    