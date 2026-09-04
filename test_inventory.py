# test_inventory.py
import pytest
from inventory import Inventory
from item import PerishableItem, ElectronicItem

@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def apple():
    return PerishableItem("りんご", 100, 10, "2026-09-10")

def test_add_item(empty_inventory, apple):
    empty_inventory.add_item(apple)
    assert len(empty_inventory.items) == 1
    assert empty_inventory.items[0].name == "りんご"

def test_add_multiple_items(empty_inventory, apple):
    earphone = ElectronicItem("イヤホン", 3000, 5)
    empty_inventory.add_item(apple)
    empty_inventory.add_item(earphone)
    assert len(empty_inventory.items) == 2

def test_empty_inventory_has_no_items(empty_inventory):
    assert len(empty_inventory.items) == 0


# test_inventory.py に追加
from unittest.mock import Mock

def test_add_item_notifies_observer(empty_inventory, apple):
    fake_observer = Mock()
    empty_inventory.add_observer(fake_observer)

    empty_inventory.add_item(apple)

    fake_observer.update.assert_called_once_with("りんごが追加されました")