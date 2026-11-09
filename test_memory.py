import pytest

from memory import Memory


def test_memory_keeps_last_messages():
    memory = Memory(limit=2)
    for text in ["раз", "два", "три"]:
        memory.add("user", text)
    assert [m["content"] for m in memory.history()] == ["два", "три"]


def test_memory_rejects_zero_limit():
    with pytest.raises(ValueError):
        Memory(limit=0)
