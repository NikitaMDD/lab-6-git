"""Реестр инструментов, которые LLM-агент может вызывать."""

TOOLS = {}


def tool(name, description):
    """Регистрирует функцию как инструмент агента."""
    def wrapper(func):
        TOOLS[name] = {"description": description, "func": func}
        return func
    return wrapper


@tool("ask_questions", "Задаёт пользователю уточняющие вопросы")
def ask_questions(questions):
    return [f"? {q}" for q in questions]


if __name__ == "__main__":
    print("Инструменты агента:")
    for name, meta in TOOLS.items():
        print(f"  - {name}: {meta['description']}")
