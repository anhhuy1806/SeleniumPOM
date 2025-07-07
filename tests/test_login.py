from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
import time

class TestLogin(BaseTest):
    def test_login_success(self):
        config = ConfigReader.get_config()
        login_page = LoginPage(self.driver)
        login_page.login(config["username"], config["password"])

        time.sleep(2)
        assert "dashboard" in self.driver.current_url.lower()
