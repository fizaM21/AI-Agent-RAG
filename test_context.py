from app.memory.conversation_memory import add_message, clear_history
from app.agents.context_resolver import resolve_query

clear_history()

add_message("user", "Who is Alan Turing?")
add_message("assistant", "Alan Turing was an English mathematician born in London.")

print(resolve_query("Where was he born?"))