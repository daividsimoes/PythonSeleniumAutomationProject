from conftest import driver
from pages.base_page import BasePage
from pages.login.login_locators import LoginLocators

class LoginPage(BasePage):


    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def login(self, username, password):
        self.enter_text(*LoginLocators.USERNAME_INPUT, username)
        self.enter_text(*LoginLocators.PASSWORD_INPUT, password)
        self.click_element(*LoginLocators.LOGIN_BUTTON)
