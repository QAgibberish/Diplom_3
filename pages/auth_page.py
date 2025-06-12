import allure
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage

class AuthPage(BasePage):
    @allure.step('Авторизация')
    def login(self, email, password):
        self.send_keys_to_input(AuthLocators.EMAIL_INPUT, email)
        self.send_keys_to_input(AuthLocators.PASSWORD_INPUT, password)
        self.click_on_element(AuthLocators.ENTER_BUTTON)