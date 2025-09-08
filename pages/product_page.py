import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_product_add_to_cart(self):
        self.browser.implicitly_wait(3)
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.get_the_cost()
        self.get_product_name()

    def add_to_cart(self):
        self.browser.implicitly_wait(3)
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        button_add_to_cart.click()

    def get_the_cost(self):
        self.browser.implicitly_wait(3)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text

        assert cart_price == product_price, f'стоимость корзины {cart_price} не совпадает ' \
                                            f'со стоимостью товара {product_price} '

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text

        assert product_name_in_cart == product_name, f'наименование товара в корзине {product_name_in_cart} ' \
                                                     f'не совпадает с добавленым в корзину товаром {product_name}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_CART), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_CART), "Success message is not disappeard, " \
                                                                               "but should not be "