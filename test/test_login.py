import pytest
from pages.login.login_page import LoginPage
from pages.main.main_page import MainPage

@pytest.mark.usefixtures("driver", "env_vars")
class TestLogin:

    @pytest.mark.dependency(name='test_login_standard_user')
    def test_login_standard_user(self, driver, env_vars):
        login_page = LoginPage(driver, env_vars.get('url'))
        login_page.login(env_vars.get('standard_user'), env_vars.get('password'))

        main_page = MainPage(driver)
        main_page.wait_main_screen_load()

        main_page_url = env_vars.get('url') + 'inventory.html'
        assert driver.current_url == main_page_url, 'URL is not from main page'

    @pytest.mark.dependency(depends=['test_login_standard_user'])
    def test_logout(self, driver, env_vars):
        main_page = MainPage(driver)
        main_page.click_hamburger_btn()
        main_page.click_logout_btn()

        assert driver.current_url == env_vars.get('url'), 'URL is not from login page'
