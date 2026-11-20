"""Logika bisnis SmartShopping, terpisah dari tampilan."""
from models import ShoppingItem

class ShoppingService:
    def __init__(self, storage):
        self.storage = storage
        self.items = storage.load_items()

    def add_item(self, name, category, quantity, price):
        if not name.strip():
            raise ValueError("Nama barang tidak boleh kosong.")
        item = ShoppingItem.create(name, category, quantity, price)
        self.items.append(item)
        self._save()
        return item

    def update_item(self, item_id, name, category, quantity, price):
        item = self.get_item(item_id)
        if not name.strip():
            raise ValueError("Nama barang tidak boleh kosong.")
        item.name = name.strip()
        item.category = category
        item.quantity = int(quantity)
        item.price = int(price)
        self._save()
        return item

    def delete_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
        self._save()

    def toggle_purchased(self, item_id):
        item = self.get_item(item_id)
        item.purchased = not item.purchased
        self._save()
        return item

    def get_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        raise ValueError("Barang tidak ditemukan.")

    def clear_items(self):
        self.items.clear()
        self._save()

    def search(self, keyword="", category="Semua", status="Semua"):
        result = self.items
        key = keyword.casefold().strip()
        if key:
            result = [item for item in result if key in item.name.casefold()]
        if category != "Semua":
            result = [item for item in result if item.category == category]
        if status == "Belum Dibeli":
            result = [item for item in result if not item.purchased]
        elif status == "Sudah Dibeli":
            result = [item for item in result if item.purchased]
        return result

    @property
    def total_cost(self):
        return sum(item.subtotal for item in self.items)

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.items)

    @property
    def purchased_count(self):
        return sum(1 for item in self.items if item.purchased)

    @property
    def pending_count(self):
        return len(self.items) - self.purchased_count

    def _save(self):
        self.storage.save_items(self.items)
