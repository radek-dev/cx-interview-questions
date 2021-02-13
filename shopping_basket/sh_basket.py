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
        if catalogue:
            self.__check_catalogue(catalogue)
        else:
            raise ValueError('Catalogue can not be empty')
        self.catalogue = catalogue

        if basket:
            self.__check_basket(basket)
        self.basket = basket if basket else {}

        if offers:
            self.__check_offers(offers)
        self.offers = offers if offers else {}

    def set_basket(self, basket: dict):
        self.__check_basket(basket)
        self.basket = basket if basket else {}

    @staticmethod
    def __check_catalogue(catalogue: dict):
        if any([not isinstance(s, str) for s in catalogue.keys()]):
            raise TypeError('Identifiers for the catalogue must be strings')
        if any([not isinstance(v, (int, float)) for v in catalogue.values()]):
            raise TypeError('Values for the catalogue must be int or float')

    def __check_basket(self, basket: dict):
        if any([not isinstance(s, str) for s in basket.keys()]):
            raise TypeError('Identifiers for the basket must be strings')
        if any([not isinstance(v, (int, float)) for v in basket.values()]):
            raise TypeError('Values for the basket must be int or float')
        if any([k not in self.catalogue.keys() for k in basket.keys()]):
            raise KeyError('The basket items must be in the catalogue')

    @staticmethod
    def __check_offers(offers: dict):
        if any([not isinstance(s, str) for s in offers.keys()]):
            raise TypeError('Identifiers for the offers must be strings')
        if any([not isinstance(v, str) for v in offers.keys()]):
            raise TypeError('Offers must be stored in dictionaries')
        # ToDo: add check for *deal* and *discount* keys, they must be present

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
            basket_quantity = self.basket[item]
            item_total = self.round(basket_quantity * self.catalogue[item])
            sub_total = self.round(sub_total + item_total)
            if item in self.offers.keys():
                if 'deal' in self.offers[item].keys() and \
                        basket_quantity >= int(self.offers[item]['deal'][0]):
                    deal_quantity = int(self.offers[item]['deal'][0])
                    item_deal_quantity = basket_quantity // deal_quantity
                    free_items = deal_quantity - int(self.offers[item]['deal'][-1])
                    item_discount = self.round(
                        (item_deal_quantity * free_items * self.catalogue[item]))
                elif 'discount' in self.offers[item].keys():
                    item_discount = self.round(
                        item_total * (self.offers[item]['discount']))

                discount = self.round(discount + item_discount)
                del item_discount

        total = self.round(sub_total - discount)
        return sub_total, discount, total

