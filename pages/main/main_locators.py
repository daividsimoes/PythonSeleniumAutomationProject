from selenium.webdriver.common.by import By

class MainLocators:

    HAMBURGER_MENU_BTN = (By.ID, 'react-burger-menu-btn')
    HAMBURGER_MENU = (By.XPATH, '*//div[@class="bm-menu"]')
    LOGOUT_BTN = (By.ID, 'logout_sidebar_link')
    PRODUCT_LABEL = (By.XPATH, '*//span[@data-test="title"]')
    CART_LINK = (By.XPATH, '*//a[@data-test="shopping-cart-link"]')
    INVENTORY_LIST = (By.XPATH, '*//div[@data-test="inventory-list"]')