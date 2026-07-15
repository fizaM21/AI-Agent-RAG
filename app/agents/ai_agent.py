from app.tools.calculator_tool import calculate
from app.tools.weather_tool import get_weather
from app.tools.wiki_tool import search_wikipedia
from app.tools.rag_tool import search_documents

from app.agents.tool_selector import choose_tool
from app.agents.context_resolver import resolve_query

from app.memory.conversation_memory import (
    add_message,
)

from app.llm.chains import chat_chain


TOOLS = {
    "calculator": calculate,
    "weather": get_weather,
    "wikipedia": search_wikipedia,
    "rag": search_documents,
}

from app.graph.workflow import agent_graph


def run_agent(query: str):

    state = {
        "query": query,
        "resolved_query": "",
        "tool": "",
        "tool_input": "",
        "tool_result": "",
        "final_answer": "",
    }

    result = agent_graph.invoke(state)

    return result["final_answer"]