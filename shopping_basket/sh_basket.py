"""
Shopping Basket Assignment for ECS
by Radek
date: 09-Feb-2021
"""


class ShoppingBasket:
    """
    It needs to be designed to be reusable.
    For any given basket, catalogue and offers your solution should return the
    sub-total, discount and total, all accurate to at least two decimal places

    This is a component which if given a selection of products chosen
    by a customer (the basket), a "catalogue" of products available in
    a supermarket and a collection of special-offers,
    can calculate the price of goods including any applicable discounts.

    The basket-pricer component is responsible for working out which offers
    are applicable to products. It will apply those offers to work out the discount
    and therefore the final price. This component is not responsible for maintaining
    the mutable state of a shopping basket. It does not need to add and remove items
    from a basket.

    No or any component which adds and removes items from the basket.

    properties:
        basket (selection by customer, basket can contain zero or more products,
        is mutable, Baskets cannot have a negative price)
        catalogue (products available in a supermarket, prices can't be hard coded,
         It's also possible that there are items in the catalogue with no offers,
         or multiple offers.)
        offers (collection of special offers, prices can't be hard coded, It's
        possible that there are offers on products
        which are no longer in the catalogue)

    methods
        get_basket_price:
            calculate the price of goods including any applicable discounts
            responsible for working out which offers are applicable to products
            apply those offers the discount and so final price
            component is not responsible for maintaining the mutable
            state of a shopping basket
            It does not need to add and remove items from a basket.
            empty basket has a sub-total, discount and total each of zero
            The discount and therefore the total price is determined by the contents
            of the basket, the undiscounted price of the goods and the applicable
            offers.


    """

    def __init__(self):
        print('hello')
        pass
