from app.agents.ai_agent import run_agent
from app.memory.conversation_memory import get_history

print(run_agent("Who is Alan Turing?"))
print(run_agent("What skills are mentioned in the resume?"))

print("\nConversation History:\n")

for message in get_history():
    print(message)