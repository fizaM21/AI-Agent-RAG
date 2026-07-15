from app.agents.ai_agent import run_agent

queries = [
    "Who is Alan Turing?",
    "Calculate 45 * 12",
    "What skills are mentioned in the resume?"
]

for query in queries:
    print("=" * 50)
    print("Query:", query)
    print("Response:", run_agent(query))