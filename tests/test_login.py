import allure
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader

@allure.epic("Login Module")
class TestLogin(BaseTest):

    #Nhập đúng email, password để test pass
    @allure.title("Login with valid credentials")
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        assert "dashboard" in self.driver.current_url.lower()

    #Nhập sai email, passsword để test fail
    @allure.title("Login with invalid credentials")
    def test_login_invalid(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalidUser", "wrongPass") #Nhập sai name
        assert "dashboard" in self.driver.current_url.lower()