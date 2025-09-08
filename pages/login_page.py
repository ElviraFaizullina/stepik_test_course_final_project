from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        assert 'login' in self.browser.current_url, 'текущий URL не соответствует ожидаемому '

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, 'форма логина отсутствует на странице'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        registration_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert registration_form, 'форма регистрации отсутствует на странице'
