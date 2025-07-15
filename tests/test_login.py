from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
import allure

@allure.epic("Login Module")
@allure.feature("OrangeHRM Login")
class TestLogin(BaseTest):

    @allure.story("Valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Login should succeed with valid credentials")
    def test_login_success(self):        
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())

      
