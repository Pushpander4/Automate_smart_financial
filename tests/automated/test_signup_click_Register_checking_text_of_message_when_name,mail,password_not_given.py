import time

from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()

def testClick_signup():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()

def test_click_button_register():
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()

def test_please_enter_your_username():
     name_alert = funtion.driver.find_element(By.XPATH,"//div[normalize-space()='Please Enter Your Username']").text
     assert (name_alert == 'Please Enter Your Username')



def test_please_enter_your_email():
    mail_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
    assert (mail_alert == 'Please Enter Your Email')


def test_please_enter_your_password():
    password_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter your password']").text
    assert (password_alert == 'Please Enter your password')
