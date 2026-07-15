from app.graph.state import AgentState

from app.memory.conversation_memory import (
    add_message,
)

from app.agents.context_resolver import resolve_query
from app.agents.tool_selector import choose_tool

from app.tools.calculator_tool import calculate
from app.tools.weather_tool import get_weather
from app.tools.wiki_tool import search_wikipedia
from app.tools.rag_tool import search_documents

from app.llm.chains import chat_chain


TOOLS = {
    "calculator": calculate,
    "weather": get_weather,
    "wikipedia": search_wikipedia,
    "rag": search_documents,
}


def resolve_context(state: AgentState):
    add_message("user", state["query"])

    resolved = resolve_query(state["query"])

    print(f"Resolved Query: {resolved}")

    state["resolved_query"] = resolved

    return state


def choose_tool_node(state: AgentState):
    selection = choose_tool(state["resolved_query"])

    print(f"Selected Tool: {selection}")

    state["tool"] = selection["tool"]
    state["tool_input"] = selection["input"]

    return state


def execute_tool(state: AgentState):

    tool = TOOLS[state["tool"]]

    result = tool.invoke(state["tool_input"])

    print(f"Tool Result:\n{result}")

    state["tool_result"] = result

    return state


def generate_response(state: AgentState):

    answer = chat_chain.invoke(
        {
            "question": state["resolved_query"],
            "tool": state["tool"],
            "tool_result": state["tool_result"],
        }
    )

    state["final_answer"] = answer

    return state


def save_memory(state: AgentState):

    add_message(
        "assistant",
        state["final_answer"]
    )

    return state