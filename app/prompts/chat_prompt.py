from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an intelligent AI assistant.

You receive:
- User question
- Tool used
- Tool result

Generate a clear, concise, and accurate answer.

If the tool result already answers the question,
don't invent additional information.
"""
        ),

        (
            "human",
            """
User Question:
{question}

Tool Used:
{tool}

Tool Result:
{tool_result}
"""
        )
    ]
)