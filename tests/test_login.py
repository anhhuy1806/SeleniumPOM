from pages.login_page import LoginPage
from time import sleep

class TestLogin:

    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        driver.implicitly_wait(10)
        assert "dashboard" in driver.current_url.lower()
        sleep(10)
