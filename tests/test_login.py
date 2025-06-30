from tests.base_test import BaseTest
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        assert "dashboard" in self.driver.current_url.lower()
