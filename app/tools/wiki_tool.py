import requests
from langchain_core.tools import tool


@tool
def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia and return a summary of the topic.
    """

    headers = {
        "User-Agent": "AI-Agent-RAG/1.0"
    }

    search_url = "https://en.wikipedia.org/w/api.php"

    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }

    search_response = requests.get(
        search_url,
        params=search_params,
        headers=headers
    )

    search_data = search_response.json()

    if not search_data["query"]["search"]:
        return "No Wikipedia article found."

    title = search_data["query"]["search"][0]["title"]

    extract_params = {
        "action": "query",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": title,
        "format": "json"
    }

    extract_response = requests.get(
        search_url,
        params=extract_params,
        headers=headers
    )

    pages = extract_response.json()["query"]["pages"]
    page = list(pages.values())[0]

    return page.get("extract", "No extract available.")