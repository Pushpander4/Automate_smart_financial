import time
from automated import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


# TODO: add a test for checking smartfinancial title image


def test_T1_email_input_field():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").is_enabled()


def test_T2_password_input_field():
    funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").is_enabled()

def test_T3_email_text():
    text_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
    assert (text_email == "Email"), 'TEST-LOGIN-1 "Email" text should be present'


def test_T4_password_text():
    text_password = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Password']").text
    assert (text_password == "Password")

def test_remember_me_text():
    text_on_remember = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Remember me']").text
    assert (text_on_remember == "Remember me")

def testremember_me():
    funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_enabled()
    funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").click()
    v1 = funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_selected()
    assert (v1 == True)

time.sleep(4)

def testlogin():
    time.sleep(4)
    funtion.login()
