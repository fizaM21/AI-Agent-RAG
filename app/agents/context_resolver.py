from app.llm.groq_llm import get_llm
from app.memory.conversation_memory import get_history

llm = get_llm()


def resolve_query(current_query: str):
    history = get_history()

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are an AI assistant.

Using the conversation history, rewrite the user's latest question so that it is fully self-contained.

Conversation:
{history_text}

Current Question:
{current_query}

Return ONLY the rewritten question.
"""

    response = llm.invoke(prompt)

    return response.content.strip()