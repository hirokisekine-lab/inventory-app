# factory

from item import PerishableItem, ElectronicItem, ClothingItem

class ItemFactory:
    @staticmethod
    def create_item(item_type, *args):
        if item_type == "perishable":
            return PerishableItem(*args)
        elif item_type == "electronic":
            return ElectronicItem(*args)
        elif item_type == "clothing":
            return ClothingItem(*args)
        else:
            raise ValueError(f"不明な商品タイプ: {item_type}")
