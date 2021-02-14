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
    sh_basket = ShoppingBasket(basket=basket, catalogue=catalogue,
                               offers=offers)
    yield sh_basket


class TestShoppingBasket:
    def test_constructor_happy_path(self, test_basket):
        # check that the instance is relevant
        assert {'get_basket_price', 'round', 'set_basket'}.issubset(
            set(dir(test_basket)))

    def test_constructor_errors(self, test_basket):
        # catalogue tests
        with pytest.raises(ValueError):
            ShoppingBasket({}, {})
        with pytest.raises(TypeError):
            ShoppingBasket({5: 5}, {})
        with pytest.raises(TypeError):
            ShoppingBasket({'test_good': 'wrong_input'}, {})
        with pytest.raises(ValueError):
            ShoppingBasket({'test_good': -1}, {})
        with pytest.raises(ValueError):
            ShoppingBasket({'test_good': 0}, {})

        # basket tests
        with pytest.raises(TypeError):
            ShoppingBasket({'test_good': 2}, {}, {5: 5})
        with pytest.raises(TypeError):
            ShoppingBasket({'test_good': 1}, {}, {'test_good': 'wrong_input'})
        with pytest.raises(KeyError):
            ShoppingBasket({'test_good': 2}, {}, {'test_good2': 2})
        with pytest.raises(ValueError):
            ShoppingBasket({'test_good': 1}, {}, {'test_good': 0})
        with pytest.raises(ValueError):
            ShoppingBasket({'test_good': 1}, {}, {'test_good': -1})

        # offer tests
        with pytest.raises(TypeError):
            ShoppingBasket({'test_good': 2}, {2: 2})
        with pytest.raises(KeyError):
            ShoppingBasket({'test_good': 2}, {'test_good': 'wrong_input'})

    def test_basket1(self, test_basket):
        basket = {'baked_beans': 4, 'biscuits': 1}
        test_basket.set_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert sub_total == 5.16
        assert discount == 0.99
        assert total == 4.17

    def test_basket2(self, test_basket):
        basket = {'baked_beans': 2, 'biscuits': 1, 'sardines': 2}
        test_basket.set_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert sub_total == 6.96
        assert discount == 1.15
        assert total == 5.81

    def test_basket3(self, test_basket):
        basket = {'baked_beans': 7, 'biscuits': 1, 'sardines': 2}
        test_basket.set_basket(basket)
        sub_total, discount, total = test_basket.get_basket_price()
        assert sub_total == 11.91
        assert discount == 2.93
        assert total == 8.98

    def test_basket4(self):
        catalogue = {
            'baked_beans': 0.99,
            'biscuits': 1.20,
            'sardines': 1.89,
            'shampoo_small': 2.00,
            'shampoo_medium': 2.50,
            'shampoo_large': 3.50,
        }
        offers = {'baked_beans': {'deal': '2-for-1', 'discount': 0.1},
                  'sardines': {'discount': 0.25},
                  'biscuits': {'deal': '5-for-1', 'discount': 0.15}}
        basket = {'baked_beans': 7, 'sardines': 1, 'biscuits': 7}
        sh_basket = ShoppingBasket(basket=basket, catalogue=catalogue,
                                   offers=offers)
        sub_total, discount, total = sh_basket.get_basket_price()
        assert sub_total == 17.22
        assert discount == 8.24
        assert total == 8.98

    def test_basket5(self):
        catalogue = {
            'baked_beans': 0.99,
            'biscuits': 1.20,
            'sardines': 1.89,
            'shampoo_small': 2.00,
            'shampoo_medium': 2.50,
            'shampoo_large': 3.50,
        }
        basket = {'baked_beans': 7, 'sardines': 1, 'biscuits': 7}
        sh_basket = ShoppingBasket(catalogue, {}, basket)
        sub_total, discount, total = sh_basket.get_basket_price()
        assert sub_total == 17.22
        assert discount == 0
        assert total == 17.22

    def test_basket6(self, test_basket):
        test_basket.set_basket({})
        sub_total, discount, total = test_basket.get_basket_price()
        assert sub_total == 0
        assert discount == 0
        assert total == 0
