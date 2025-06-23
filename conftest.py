import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    sleep(3)
    yield driver
    driver.quit()
