import pytest
from selenium import webdriver

class DriverSetup:
    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3) 
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()

driver_setup_instance = DriverSetup()

@pytest.fixture(scope="function")
def driver(request):
    driver = driver_setup_instance.start()

    def teardown():
        driver_setup_instance.quit()

    request.addfinalizer(teardown)
    return driver
