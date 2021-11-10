import json
from typing import Dict


def serialize(d: Dict) -> str:
    return json.dumps(d, default=lambda o: vars(o), indent=4)
