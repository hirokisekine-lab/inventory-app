from factory import ItemFactory
from item import GiftWrapDecorator, MessageCardDecorator
"""
apple = ItemFactory.create_item("perishable", "りんご", 100, 10, "2026-09-10")
wrapped_apple = GiftWrapDecorator(apple)
special_apple = MessageCardDecorator(wrapped_apple)  # ラッピング + メッセージカード

print(special_apple)                          # ?
print(special_apple.get_discounted_price())    # ?

# Inventoryに追加しても、普通のItemと同じように扱えることを確認
from inventory import Inventory
inventory = Inventory()
inventory.add_item(special_apple)
inventory.show_all()
inventory.show_discounted_prices()
"""
from unittest.mock import Mock

fake_notifier = Mock()
fake_notifier.update("テストメッセージ")

# 本当にupdateが呼ばれたか確認
print(fake_notifier.update.called)              # ?
print(fake_notifier.update.call_args)            # ?
