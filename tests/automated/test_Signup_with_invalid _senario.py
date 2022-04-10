import time

from automated import funtion
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


funtion.open_browser()

#when no details are entered for sign up . checking waring message
#(Working)
def test_click_signup():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()
def test_click_button_register():
    funtion.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()
def test_Please_enter_you_first_name():
    Please_enter_you_first_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your first name']").text
    assert (Please_enter_you_first_name == 'Please enter your first name')
def test_Please_enter_your_last_name():
    Please_enter_your_last_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your last name']").text
    assert (Please_enter_your_last_name == 'Please enter your last name')
def test_Please_select_a_time_zone():
    Please_select_a_time_zone = funtion.driver.find_element(By.XPATH, "//span[normalize-space()='Please select a time zone']").text
    assert (Please_select_a_time_zone == 'Please select a time zone')
def test_Please_enter_your_address():
    Please_enter_your_address = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your address']").text
    assert (Please_enter_your_address == 'Please enter your address')
def test_Please_enter_your_city():
    Please_enter_your_city = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your city']").text
    assert (Please_enter_your_city == 'Please enter your city')
def test_Please_enter_your_state():
    Please_enter_your_city = funtion.driver.find_element(By.XPATH, "//span[normalize-space()='Please select your state']").text
    assert (Please_enter_your_city == 'Please select your state')
def test_Please_enter_your_zip():
    Please_enter_your_zip = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your zip']").text
    assert (Please_enter_your_zip == 'Please enter your zip')
def test_Please_enter_a_valid_email():
    Please_enter_a_valid_email = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter a valid email']").text
    assert (Please_enter_a_valid_email == 'Please enter a valid email')
def test_Please_enter_your_password():
    Please_enter_your_password = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your password']").text
    assert (Please_enter_your_password == 'Please enter your password')




#try to  signup with already taken email

#function.driver.back()

def test_click_signup():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()
    time.sleep(2)

def test_enter_signup_details():
    funtion.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
    funtion.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("XYZ")
    funtion.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("2345672347")
    funtion.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fgdwbhgbgibgibgjgjdjgad djgndgijjndgjsdn")
    funtion.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Delhi")
    funtion.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12345")
    funtion.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("piyush@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Abcderfgh1@")
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()


    time.sleep(5)
