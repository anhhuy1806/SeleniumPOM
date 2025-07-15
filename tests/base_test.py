import time
import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook để lấy kết quả test
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_call" + rep.when, rep)

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver
        yield
        self.driver.quit()