import json

from app.llm.groq_llm import get_llm
from app.memory.conversation_memory import get_history
from app.models.tool_schema import ToolSelection
llm = get_llm()


def choose_tool(query: str):
    history = get_history()

    history_text = ""

    for message in history:
        history_text += f"{message['role']}: {message['content']}\n"

    prompt = f"""
You are an AI routing agent.

Conversation History:
{history_text}

Choose the best tool and extract the correct input.

Available tools:
- calculator
- weather
- wikipedia
- rag

Rules:

calculator:
Return the mathematical expression only.
Example:
{{
    "tool": "calculator",
    "input": "45 * 12"
}}

weather:
Return only the city.
Example:
{{
    "tool": "weather",
    "input": "Bangalore"
}}

wikipedia:
Return only the person or topic.
Example:
{{
    "tool": "wikipedia",
    "input": "Alan Turing"
}}

rag:
Return only the document question.
Example:
{{
    "tool": "rag",
    "input": "What skills are mentioned in the resume?"
}}

Return ONLY valid JSON.
Do NOT wrap the JSON inside ```json or ```.

Current User Query:
{query}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    print("LLM Response:", content)

    # Remove markdown code fences if the model still returns them
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    return json.loads(content)