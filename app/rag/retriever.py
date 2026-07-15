from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def get_retriever(vector_db_path="vector_db"):
    """
    Load the FAISS vector database and return a retriever.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.load_local(
        vector_db_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever