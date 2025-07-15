from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        username_element = self.wait_element(self.username_input) 
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.wait_element(self.password_input) 
        password_element.send_keys(password) 

    def click_login(self):
        self.click(self.login_button) 

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(10)  
        
    def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.username_input)
    )
