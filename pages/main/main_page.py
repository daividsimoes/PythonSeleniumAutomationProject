from pages.base_page import BasePage
from pages.main.main_locators import MainLocators
from pages.login.login_locators import LoginLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_main_screen_load(self):
        self.wait_visibility_of_element(*MainLocators.HAMBURGER_MENU_BTN)
        self.wait_visibility_of_element(*MainLocators.PRODUCT_LABEL)
        self.wait_visibility_of_element(*MainLocators.CART_LINK)
        self.wait_visibility_of_element(*MainLocators.INVENTORY_LIST)

    def click_hamburger_btn(self):
        self.click_element(*MainLocators.HAMBURGER_MENU_BTN)
        self.wait_visibility_of_element(*MainLocators.HAMBURGER_MENU)

    def click_logout_btn(self):
        self.click_element(*MainLocators.LOGOUT_BTN)
        self.wait_visibility_of_element(*LoginLocators.LOGIN_BUTTON)
