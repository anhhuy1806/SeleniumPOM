import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader

class BaseTest:
    driver = None

    @pytest.fixture(autouse=True)
    def setup(self):
        config = ConfigReader.get_config()
        BaseTest.driver = webdriver.Chrome()
        BaseTest.driver.get(config["url"])
        BaseTest.driver.maximize_window()
        yield
        BaseTest.driver.quit()
