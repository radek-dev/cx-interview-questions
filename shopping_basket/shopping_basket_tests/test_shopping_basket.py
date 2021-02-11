import pytest

from shopping_basket.sh_basket import ShoppingBasket


class TestShoppingBasket:
    def test_constructor_happy_path(self):
        sh = ShoppingBasket()
        assert True