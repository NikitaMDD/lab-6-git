"""Краткосрочная память агента: последние сообщения диалога."""


class Memory:
    def __init__(self, limit=20):
        if limit < 1:
            raise ValueError("limit должен быть больше нуля")
        self.limit = limit
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.limit:
            self.messages = self.messages[-self.limit:]

    def history(self):
        return list(self.messages)
