from langchain_core.tools import tool

from app.rag.retriever import get_retriever


@tool
def search_documents(query: str) -> str:
    """
    Search the vector database and return relevant documents.
    """

    retriever = get_retriever()

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found."

    return "\n\n".join(doc.page_content for doc in docs)