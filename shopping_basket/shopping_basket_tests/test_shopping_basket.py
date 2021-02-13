import pytest

from shopping_basket.sh_basket import ShoppingBasket


@pytest.fixture(scope='module')
def test_basket():
    catalogue = {
        'baked_beans': 0.99,
        'biscuits': 1.20,
        'sardines': 1.89,
        'shampoo_small': 2.00,
        'shampoo_medium': 2.50,
        'shampoo_large': 3.50,
    }
    offers = {'baked_beans': {'deal': '3-for-2', 'discount': 0.1},
              'sardines': {'discount': 0.25}}
    sh_basket = ShoppingBasket(catalogue=catalogue, offers=offers)
    yield sh_basket


class TestShoppingBasket:
    def test_constructor_example1(self, test_basket):
        basket = {'baked_beans': 4, 'biscuits': 1}
        test_basket.add_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert 5.16 == sub_total
        assert 0.99 == discount
        assert 4.17 == total

    def test_constructor_example2(self, test_basket):
        basket = {'baked_beans': 2, 'biscuits': 1, 'sardines': 2}
        test_basket.add_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert 6.96 == sub_total
        assert 1.15 == discount
        assert 5.81 == total

# ToDo: add more cases
