from time import time

from nextcord import Message


class Timer:
    def __init__(self,
                 remaining: float,
                 message: Message):
        self._remaining = remaining
        self._message = message
        self.update_end()

    def update_remaining(self):
        self._remaining = self._end - time()

    def update_end(self):
        self._end = time() + self._remaining

    def get_remaining(self) -> float:
        return self._remaining

    def get_end(self) -> float:
        return self._end

    def get_message(self) -> Message:
        return self._message
