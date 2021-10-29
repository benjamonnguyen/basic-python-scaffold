from abc import ABC
import json


class Message(ABC):
    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: vars(o), indent=4)
