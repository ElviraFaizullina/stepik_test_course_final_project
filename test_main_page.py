from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    """checks that the guest can see the login link"""
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    """checks that the guest can go to the login page"""
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """checks guest cant see product in basket opened from main page"""
    link_main_page = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = MainPage(browser, link_main_page)
    page.open()
    basket_page = page.open_basket()
    basket_page.is_basket_empty()
    basket_page.there_is_no_product_in_cart()
