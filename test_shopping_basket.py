import unittest
from ShoppingBasket.shopping_basket import ShoppingBasket


def test_items_exist_in_empty_shopping_basket():
    sb = ShoppingBasket()
    assert isinstance(sb.items, list) is True




