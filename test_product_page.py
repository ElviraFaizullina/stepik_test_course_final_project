import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


URLS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                     marks=pytest.mark.xfail(reason="Ссылка временно не работает")),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', URLS)
def test_guest_can_add_product_to_basket(browser, link):
    """checks guest cant add product to basket"""
    page = ProductPage(browser, link)
    page.open()
    page.should_product_add_to_cart()


@pytest.mark.need_review
@pytest.mark.xfail
@pytest.mark.parametrize('link', URLS)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """checks success  message disappeared after adding product to basket
    Args:
        link: links to all online stores
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_product_add_to_cart()
    page.should_disappeared_success_message()


@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    """checks guest should see login link on product page"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """checks guest can go to login page from product page"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """checks guest can see product in basket opened from product page"""
    link_shop = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link_shop)
    page.open()
    basket_page = page.open_basket()
    basket_page.is_basket_empty()
    basket_page.there_is_no_product_in_cart()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    """checks thart User can add product to basket from product page"""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """registration new user"""
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        """checks that user add product to basket"""
        link1 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link1)
        page.open()
        page.should_product_add_to_cart_without_action()

    def test_user_cant_see_success_message(self, browser):
        """checks that user cant see success message about the successful addition of an item to the shopping cart"""
        link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link2)
        page.open()
        page.should_not_be_success_message()
