from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '.alertinner strong')
