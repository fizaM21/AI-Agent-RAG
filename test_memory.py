from app.memory.conversation_memory import (
    add_message,
    get_history,
    clear_history
)

clear_history()

add_message("user", "Who is Alan Turing?")
add_message("assistant", "Alan Turing was a mathematician.")

print(get_history())