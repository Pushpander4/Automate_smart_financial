import time

from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()


def test_text_of_forgot_password():
    text_of_sign_in_with = funtion.driver.find_element(By.XPATH,"//a[@class='text-muted']").text
    assert (text_of_sign_in_with == "Forgot your password?"), 'TEST-13 "Forgot your password?" should be present'

def test_Forgot_password_enable():
    funtion.driver.find_element(By.XPATH,"//a[@class='text-muted']").is_enabled()

def test_Click_forgot_password():
    funtion.driver.find_element(By.XPATH,"//a[@class='text-muted']").click()
    time.sleep(3)

def testIn_forgot_password_email():
    text_of_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
    assert (text_of_email == "Email")

def test_text_2022_Smart_Financial():
    t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 SmartFinancial']").text
    assert (t_2022_Smart_Financial == "© 2022 SmartFinancial")

def testIn_email_enable():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").is_enabled()


def testIn_email_place_holder():
    place_holder_on_email_place_holder = funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").get_attribute("placeholder")
    assert (place_holder_on_email_place_holder == "Enter email")

def test_enter_the_email_for_reseting_of_password():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("sheerin@example.com")


def testtext_on_reset_button():
    text_on_reset_button = funtion.driver.find_element(By.XPATH,"//button[@type='submit']").text
    assert (text_on_reset_button == "Reset")

def test_click_on_reset_button_enble():
    funtion.driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()

def test_click_on_reset_button():
    funtion.driver.find_element(By.XPATH,"//button[@type='submit']").click()




# def testReset_link_text():
#     text_on_Reset_link_text = funtion.driver.find_element(By.XPATH,"//div[@role='alert']").text
#     assert (text_on_Reset_link_text == "Reset link are sended to your mailbox, check there first")


def testbacktologin():
    text_on_login_back = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
    assert (text_on_login_back == "Login")

def test_click_on_login_button_to_go_back_to_login_page():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()