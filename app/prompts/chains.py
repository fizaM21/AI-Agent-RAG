from langchain_core.output_parsers import StrOutputParser

from app.llm.groq_llm import get_llm
from app.prompts.chat_prompt import chat_prompt

llm = get_llm()

chat_chain = (
    chat_prompt
    | llm
    | StrOutputParser()
)