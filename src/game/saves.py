from yaml import load, Loader
from typing import Any


def load_saves() -> dict[str, Any]:
    with open("savegame.yaml", "r", encoding="utf-8") as file:
        data = load(file, Loader)

        return data['players']
