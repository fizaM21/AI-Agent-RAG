from langgraph.graph import StateGraph, END

from app.graph.state import AgentState
from app.graph.nodes import (
    resolve_context,
    choose_tool_node,
    execute_tool,
    generate_response,
    save_memory,
)

workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("resolve_context", resolve_context)
workflow.add_node("choose_tool", choose_tool_node)
workflow.add_node("execute_tool", execute_tool)
workflow.add_node("generate_response", generate_response)
workflow.add_node("save_memory", save_memory)

# Set entry point
workflow.set_entry_point("resolve_context")

# Connect nodes
workflow.add_edge("resolve_context", "choose_tool")
workflow.add_edge("choose_tool", "execute_tool")
workflow.add_edge("execute_tool", "generate_response")
workflow.add_edge("generate_response", "save_memory")
workflow.add_edge("save_memory", END)

# Compile graph
agent_graph = workflow.compile()