from typing import Literal
from pydantic import BaseModel


class ToolSelection(BaseModel):
    tool: Literal[
        "calculator",
        "weather",
        "wikipedia",
        "rag",
    ]
    input: str