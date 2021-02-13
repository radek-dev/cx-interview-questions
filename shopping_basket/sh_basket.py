"""
Shopping Basket Assignment for ECS
by Radek
date: 09-Feb-2021
"""
from decimal import Decimal as Dec
from decimal import ROUND_HALF_UP as RHU


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
        possible that there are offers on products which are no longer in the catalogue)

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
    def __init__(self, catalogue: dict, offers: dict, basket: dict = {}):
        # ToDo: add error handling for inputs
        self.basket = basket
        self.catalogue = catalogue if catalogue else {}
        self.offers = offers if offers else {}

    def add_basket(self, basket: dict):
        self.basket = basket if basket else {}

    @staticmethod
    def round(number: float, places: int = 2) -> float:
        number = str(number)
        place = ['1.']
        place.extend(['0'] * places)
        return float(Dec(number).quantize(Dec(''.join(place)), rounding=RHU))

    def get_basket_price(self) -> tuple:
        sub_total, discount, total = 0, 0, 0

        for item in self.basket.keys():
            # item_total = quantity * price
            item_total = self.round(self.basket[item] * self.catalogue[item])
            sub_total = self.round(sub_total + item_total)
            if item in self.offers.keys():
                if 'deal' in self.offers[item].keys() and\
                        self.basket[item] >= int(self.offers[item]['deal'][0]):
                    item_deal_quantity = self.basket[item] // int(
                        self.offers[item]['deal'][0])
                    free_items = (int(self.offers[item]['deal'][0]) - int(
                        self.offers[item]['deal'][-1]))
                    item_discount = self.round(
                        (item_deal_quantity * free_items * self.catalogue[item]))
                    discount = self.round(discount + item_discount)
                elif 'discount' in self.offers[item].keys():
                    item_discount = self.round(
                        item_total * (self.offers[item]['discount']))
                    discount = self.round(discount + item_discount)
                del item_discount

        total = self.round(sub_total - discount)
        return sub_total, discount, total

