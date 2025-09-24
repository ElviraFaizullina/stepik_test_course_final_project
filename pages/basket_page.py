from .locators import *
from .base_page import BasePage


class BasketPage(BasePage):
    def is_basket_empty(self):
        """checking that the shopping cart is empty"""
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'The basket is not empty'

    def there_is_no_product_in_cart(self):
        """checking that there are no product in the basket"""
        self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "There's something in the basket."
