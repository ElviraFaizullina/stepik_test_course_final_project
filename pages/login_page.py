from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """checking the login page display"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """checking the login url display"""
        assert 'login' in self.browser.current_url, 'the current URL does not match the expected one'

    def should_be_login_form(self):
        """checking the login page display"""
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, 'the login form is missing on the page'

    def should_be_register_form(self):
        """checking the registration form display"""
        registration_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert registration_form, 'the registration form is missing on the page'

    def register_new_user(self, email, password):
        """user registration
        Args:
            email: user's email address
            password: user's password
        """
        self.browser.implicitly_wait(3)
        self.should_be_register_form()
        button_register_email_address = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_EMAIL)
        button_register_email_address.send_keys(email)
        button_register_password = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_PASSWORD)
        button_register_password.send_keys(password)
        button_register_password_confirm = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_CONFIRM_PASSWORD)
        button_register_password_confirm.send_keys(password)
        button_confirm = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_SUBMIT)
        button_confirm.click()
