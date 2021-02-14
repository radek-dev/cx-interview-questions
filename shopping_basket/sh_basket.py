"""
Shopping Basket Assignment for ECS
by Radek
date: 09-Feb-2021
Python 3.8
"""
from decimal import Decimal as Dec
from decimal import ROUND_HALF_UP as RHU


class ShoppingBasket:
    """
    This is a dictionary based implementation of the shopping basket class.
    It consists of 3 private dictionaries.
    """
    def __init__(self, catalogue: dict, offers: dict, basket: dict = {}):
        """
        ShoppingBaske constructors checks for validity of inputs and
        set the properties.

        Args:
            catalogue (dict): dictionary of items and prices
            offers (dict): dictionary of offers
            basket (dict): dictionary of basket goods
        """
        if catalogue:
            self.__check_catalogue(catalogue)
        else:
            raise ValueError('Catalogue can not be empty')
        self.__catalogue = catalogue

        if basket:
            self.__check_basket(basket)
        self.__basket = basket if basket else {}

        if offers:
            self.__check_offers(offers)
        self.__offers = offers if offers else {}

    def set_basket(self, basket: dict):
        """
        The method is only for testing as it was not really required.
        It works like the constructor

        Args:
            basket (dict): dictionary with basket
        """
        self.__check_basket(basket)
        self.__basket = basket if basket else {}

    @staticmethod
    def __check_catalogue(catalogue: dict):
        """
        Checks the validity of entries in the catalogue

        Args:
            catalogue (dict): dictionary with values
        """
        if any([not isinstance(s, str) for s in catalogue.keys()]):
            raise TypeError('Identifiers for the catalogue must be strings')
        if any([not isinstance(v, (int, float)) for v in catalogue.values()]):
            raise TypeError('Values for the catalogue must be int or float')
        if any([v <= 0 for v in catalogue.values()]):
            raise ValueError(
                'All values in the catalogue must be greater than zero')

    def __check_basket(self, basket: dict):
        """
        Checks the validity of the basket entries.
        Args:
            basket: basket of goods with positive values. Values are integers
        """
        if any([not isinstance(s, str) for s in basket.keys()]):
            raise TypeError('Identifiers for the basket must be strings')
        if any([not isinstance(v, int) for v in basket.values()]):
            raise TypeError('Values for the basket must be int or float')
        if any([k not in self.__catalogue.keys() for k in basket.keys()]):
            raise KeyError('The basket items must be in the catalogue')
        if any([v <= 0 for v in basket.values()]):
            raise ValueError(
                'All values in the basket must be greater than zero')

    @staticmethod
    def __check_offers(offers: dict):
        """
        Check the validity of offers. This is nested dictionary.
        NOTE: I have some test outstanding here.

        Args:
            offers (dict): dictionary with offers
        """
        if any([not isinstance(s, str) for s in offers.keys()]):
            raise TypeError('Identifiers for the offers must be strings')
        for item in offers.keys():
            if any([s not in ['deal', 'discount'] for s in offers[item]]):
                raise KeyError(
                    'Offers must include deal or discount keys only')
        # ToDo: there are missing checks for correct offer inputs here

    @staticmethod
    def round(number: float, places: int = 2) -> float:
        """
        This is custom rounding methods. It rounds always half up.

        Args:
            number (float): the number to round
            places (int): number of decimal places to work with

        Returns:
            float:

        """
        number = str(number)
        place = ['1.']
        place.extend(['0'] * places)
        return float(Dec(number).quantize(Dec(''.join(place)), rounding=RHU))

    def __get_item_discount(self, item: str) -> float:
        """
        Method for calculating the discount value for percentage discount type
        Args:
            item (str): good from the basket

        Returns:
            float: the actual value of the discount based on the percentage.

        """
        item_total = self.round(self.__basket[item] * self.__catalogue[item])
        item_discount = self.round(
            item_total * (self.__offers[item]['discount']))
        return item_discount

    def __get_item_deal(self, item: str) -> float:
        """
        Calculates the discount based on the deal offer.

        Args:
            item (str): good from the basket

        Returns:
            float: the actual discount value based on the offer.
        """
        deal_quantity = int(self.__offers[item]['deal'][0])
        item_deal_quantity = self.__basket[item] // deal_quantity
        free_items = deal_quantity - int(self.__offers[item]['deal'][-1])
        item_deal = self.round(
            (item_deal_quantity * free_items * self.__catalogue[item]))
        return item_deal

    def get_basket_price(self) -> tuple:
        """
        Works out which offers are applicable to basket of goods and returns
        the prices of the basket.

        Returns:
            tuple: The tuple with 3 float values, sub_total, discount, total
        """
        sub_total, discount, total = 0, 0, 0

        if self.__basket:
            for item in self.__basket.keys():
                # item_total = quantity * price
                item_total = self.round(
                    self.__basket[item] * self.__catalogue[item])
                sub_total = self.round(sub_total + item_total)
                if self.__offers and item in self.__offers.keys():
                    item_discount = 0

                    if 'deal' in self.__offers[item].keys() and self.__basket[
                            item] >= int(self.__offers[item]['deal'][0]):
                        item_discount = self.__get_item_deal(item)
                    elif 'discount' in self.__offers[item].keys():
                        item_discount = self.__get_item_discount(item)

                    discount = self.round(discount + item_discount)
                    del item_discount

        total = self.round(sub_total - discount)
        return sub_total, discount, total
