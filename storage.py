"""Pengelolaan penyimpanan data JSON."""
import json
from pathlib import Path
from config import DATA_FILE
from models import ShoppingItem

class ShoppingStorage:
    def __init__(self, filename=DATA_FILE):
        self.path = Path(filename)

    def load_items(self):
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as file:
                raw = json.load(file)
            return [ShoppingItem.from_dict(row) for row in raw]
        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
            return []

    def save_items(self, items):
        payload = [item.to_dict() for item in items]
        temporary = self.path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=4, ensure_ascii=False)
        temporary.replace(self.path)
