# test_factory.py
import pytest
from factory import ItemFactory

def test_create_item_perishable():
    item = ItemFactory.create_item("perishable", "りんご", 100, 10, "2026-09-10")
    assert item.name == "りんご"

def test_create_item_invalid_type_raises_error():
    with pytest.raises(ValueError):
        ItemFactory.create_item("unknown_type", "何か", 100, 1)
