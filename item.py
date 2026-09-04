#Strategy

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_discounted_price(self):
        pass  # pragma: no cover

    def __str__(self):
        return f"{self.name}: {self.price}円 (在庫: {self.quantity})"

class PerishableItem(Item):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"{self.name}: {self.price}円 (在庫: {self.quantity}) 有効期限: {self.expiration_date}"
    
    def get_discounted_price(self):
        return self.price * 0.9

class ElectronicItem(Item):
    def get_discounted_price(self):
        return self.price

class ClothingItem(Item):
    def get_discounted_price(self):
        return self.price * 0.8


# Decorator

class ItemDecorator(Item):
    def __init__(self, item):
        self.item = item

    @property
    def name(self):
        return self.item.name

    @property
    def price(self):
        return self.item.price

    @property
    def quantity(self):
        return self.item.quantity

    def get_discounted_price(self):
        return self.item.get_discounted_price()

    def __str__(self):
        return str(self.item)


class GiftWrapDecorator(ItemDecorator):
    def get_discounted_price(self):
        return self.item.get_discounted_price() + 50

    def __str__(self):
        return f"{self.item}(ギフトラッピング)"


class MessageCardDecorator(ItemDecorator):
    def get_discounted_price(self):
        return self.item.get_discounted_price() + 30

    def __str__(self):
        return f"{self.item}(メッセージカード付き)"