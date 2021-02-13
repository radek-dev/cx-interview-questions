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
    basket = {'baked_beans': 4, 'biscuits': 1}
    sh_basket = ShoppingBasket(basket=basket, catalogue=catalogue, offers=offers)
    yield sh_basket


class TestShoppingBasket:
    def test_constructor_happy_path(self, test_basket):
        assert isinstance(test_basket.basket, dict)
        assert isinstance(test_basket.catalogue, dict)
        assert isinstance(test_basket.offers, dict)
        assert all([isinstance(s, str) for s in test_basket.basket.keys()])
        assert all([isinstance(s, str) for s in test_basket.catalogue.keys()])
        assert all([isinstance(s, str) for s in test_basket.offers.keys()])
        assert all([isinstance(v, (int, float))
                    for v in test_basket.basket.values()])
        assert all([isinstance(v, (int, float))
                    for v in test_basket.catalogue.values()])
        assert all([isinstance(v, dict)
                    for v in test_basket.offers.values()])
        for offer in test_basket.offers.keys():
            assert all(
                [isinstance(s, str) for s in test_basket.offers[offer].keys()])
            assert all([isinstance(v, (int, float, str)) for v in
                        test_basket.offers[offer].values()])

    def test_constructor_errors(self, test_basket):
        # I would put the error cases here.
        # The exercise doesn't seem to require this.
        # I found this easy to deal with.
        pass

    def test_example1(self, test_basket):
        basket = {'baked_beans': 4, 'biscuits': 1}
        test_basket.set_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert 5.16 == sub_total
        assert 0.99 == discount
        assert 4.17 == total

    def test_example2(self, test_basket):
        basket = {'baked_beans': 2, 'biscuits': 1, 'sardines': 2}
        test_basket.set_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert 6.96 == sub_total
        assert 1.15 == discount
        assert 5.81 == total

# ToDo: add more cases for edge cases
