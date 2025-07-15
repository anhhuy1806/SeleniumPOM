import os
import time
import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
import allure

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver

        #tạo folder screenshots
        os.makedirs("screenshots", exist_ok=True)
        yield
        
        # Screenshot sau mỗi test (pass hoặc fail)
        test_name = request.node.name
        filename = f"{test_name}.png"
        filepath = os.path.join("screenshots", filename)
        self.driver.save_screenshot(filepath)
        allure.attach.file(filepath, name=test_name, attachment_type=allure.attachment_type.PNG)
        self.driver.quit()
