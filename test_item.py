# test_item.py
from item import PerishableItem, ElectronicItem, ClothingItem, GiftWrapDecorator, MessageCardDecorator

def test_perishable_item_discount():
    item = PerishableItem("りんご", 100, 10, "2026-09-10")
    assert item.get_discounted_price() == 90

def test_electronic_item_discount():
    item = ElectronicItem("イヤホン", 3000, 5)
    assert item.get_discounted_price() == 3000  # 割引なし

def test_clothing_item_discount():
    item = ClothingItem("Tシャツ", 2000, 15)
    assert item.get_discounted_price() == 1600  # 20%引き



def test_gift_wrap_decorator():
    item = PerishableItem("りんご", 100, 10, "2026-09-10")
    wrapped = GiftWrapDecorator(item)
    assert wrapped.get_discounted_price() == 90 + 50
    assert wrapped.name == "りんご"
    assert wrapped.price == 100
    assert wrapped.quantity == 10
    assert "ギフトラッピング" in str(wrapped)

def test_message_card_decorator_stacked():
    item = PerishableItem("りんご", 100, 10, "2026-09-10")
    wrapped = GiftWrapDecorator(item)
    special = MessageCardDecorator(wrapped)
    assert special.get_discounted_price() == 90 + 50 + 30
    assert "メッセージカード" in str(special)

def test_item_str_representation():
    item = ElectronicItem("イヤホン", 3000, 5)
    assert str(item) == "イヤホン: 3000円 (在庫: 5)"


from item import ItemDecorator

def test_item_decorator_passthrough():
    item = PerishableItem("りんご", 100, 10, "2026-09-10")
    decorated = ItemDecorator(item)

    assert decorated.get_discounted_price() == 90
    assert str(decorated) == str(item)

