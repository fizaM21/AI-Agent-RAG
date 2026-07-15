from app.tools.calculator import calculator
from app.tools.weather_tool import get_weather
from app.tools.wikipedia_tool import search_wikipedia


TOOLS = {
    "calculator": calculator,
    "weather": get_weather,
    "wikipedia": search_wikipedia
}


def execute_tool(tool_name, query):

    if tool_name in TOOLS:
        return TOOLS[tool_name](query)

    return "Tool not found"