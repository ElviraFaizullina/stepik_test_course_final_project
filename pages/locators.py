from selenium.webdriver.common.by import By


class MainPageLocators():
    """
    Contains locators for elements on the MainPage
    LOGIN_LINK: Locator for  "Login" button
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """
    Contains locators for elements on the LoginPage

    LOGIN_FORM: Locator for login form
    REGISTER_FOR: Locator for registration form
    INPUT_REGISTER_EMAIL: Locator for email field in registration form
    INPUT_REGISTER_PASSWORD: Locator for password field in registration form
    INPUT_REGISTER_CONFIRM_PASSWORD:Locator for password confirm field in registration form
    BUTTON_REGISTER_SUBMIT:Locator for "Submit" button in registration form

    """
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, '[name=registration-email]')
    INPUT_REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password1]')
    INPUT_REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password2]')
    BUTTON_REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators():
    """
    Contains locators for elements on the ProductPage

    BUTTON_ADD_TO_CARD: Locator for "Add to card" button
    CART_PRICE: Locator for cart price element
    PRODUCT_PRICE: Locator for product price element
    PRODUCT_NAME: Locator for product name element
    PRODUCT_NAME_IN_CART:Locator for product name in cart

    """
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '.alertinner strong')


class BasePageLocators():
    """
    Contains locators for elements on the BasePage

    USER_ICON: Locator for user icon
    BUTTON_OPEN_BASKET: Locator for "Open Basket" button
    """
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_OPEN_BASKET = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')


class BasketPageLocators():
    """Contains locators for elements on the
    EMPTY_BASKET: Locator for empty basket element
    ITEMS_IN_BASKET: Locator for items in basket element
    """
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-6.h3')
