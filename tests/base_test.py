from selenium import webdriver

class BaseTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
