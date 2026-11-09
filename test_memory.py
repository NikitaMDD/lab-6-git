from memory import Memory


def test_memory_keeps_last_messages():
    memory = Memory(limit=2)
    for text in ["раз", "два", "три"]:
        memory.add("user", text)
    assert [m["content"] for m in memory.history()] == ["два", "три"]
