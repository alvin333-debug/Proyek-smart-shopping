"""Model dan validasi item belanja."""
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

@dataclass
class ShoppingItem:
    id: str
    name: str
    category: str
    quantity: int
    price: int
    purchased: bool = False
    created_at: str = ""

    @property
    def subtotal(self):
        return self.quantity * self.price

    @classmethod
    def create(cls, name, category, quantity, price):
        return cls(
            id=str(uuid.uuid4()),
            name=name.strip(),
            category=category,
            quantity=int(quantity),
            price=int(price),
            purchased=False,
            created_at=datetime.now().isoformat(timespec="seconds"),
        )

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            category=data.get("category", "Lainnya"),
            quantity=int(data.get("quantity", 1)),
            price=int(data.get("price", 0)),
            purchased=bool(data.get("purchased", False)),
            created_at=data.get("created_at", ""),
        )
