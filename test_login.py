from time import sleep
# def test_title(driver):
#     assert "OrangeHRM" in driver.title

def test_login_success(driver):
  
    username_input = driver.find_element("name", "username")
    username_input.send_keys("Admin")

    
    password_input = driver.find_element("name", "password")
    password_input.send_keys("admin123")

    
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()

   
    driver.implicitly_wait(10)
    assert "dashboard" in driver.current_url.lower()
    sleep(10) 