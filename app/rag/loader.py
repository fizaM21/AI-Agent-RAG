from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Loads a PDF and returns a list of LangChain Document objects.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents