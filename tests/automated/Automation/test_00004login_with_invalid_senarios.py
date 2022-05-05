import time
from Automation import function

from selenium.webdriver.common.by import By


function.open_browser()

#when both fields (email and name are empty) and log in button is clicked.

def test_Click_login():
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


def test_please_enter_your_email():
    email_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
    assert (email_alert == 'Please Enter Your Email')


def test_please_enter_your_password():
    password_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
    assert (password_alert == 'Please Enter Your Password')

#enter email , don't enter password and log in button is clicked.
def test_enter_email_not_password():
    function.driver.refresh()
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@ikshalabs.com')
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    password_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
    assert (password_alert == 'Please Enter Your Password')
    time.sleep(2)
#enter password , don't enter email and log in button is clicked.
def test_enter_password_not_email():
    function.driver.refresh()
    time.sleep(3)
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@123")
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    email_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
    assert (email_alert == 'Please Enter Your Email')


#enter invalid email
def test_invalid_email():
    function.driver.refresh()
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@.com')
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    invalid_mail_alert = function.driver.find_element(By.XPATH, "//div[@type='invalid']").text
    assert (invalid_mail_alert == 'email must be a valid email')


#correct email and invalid password
def test_invalid_password():
    function.driver.refresh()
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@ikshalabs.com')
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys('piyush@123')
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(6)
    invalid_password_alert = function.driver.find_element(By.XPATH, "//div[@role='alert']").text
    assert (invalid_password_alert == 'Invalid credentials')
