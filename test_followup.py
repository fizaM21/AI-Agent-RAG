from app.agents.ai_agent import run_agent
from app.memory.conversation_memory import clear_history

clear_history()

print("USER:", "Who is Alan Turing?")
print("AI:", run_agent("Who is Alan Turing?"))

print("\nUSER:", "Where was he born?")
print("AI:", run_agent("Where was he born?"))