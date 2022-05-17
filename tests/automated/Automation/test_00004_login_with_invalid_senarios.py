import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest

function.open_browser()
@pytest.mark.usefixtures("get_data")
# when both fields (email and name are empty) and log in button is clicked.
class TestInvalidLogin:
    def test_click_login(self):
        function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def test_please_enter_your_email(self):
        email_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
        assert (email_alert == 'Please Enter Your Email')

    def test_please_enter_your_password(self):
        password_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
        assert (password_alert == 'Please Enter Your Password')

    # enter email, don't enter password and log in button is clicked.
    def test_enter_email_not_password(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@ikshalabs.com')
        function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        password_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
        assert (password_alert == 'Please Enter Your Password')
        time.sleep(2)

    # enter password, don't enter email and log in button is clicked.
    def test_enter_password_not_email(self):
        function.driver.refresh()
        time.sleep(3)
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@123")
        function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        email_alert = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
        assert (email_alert == 'Please Enter Your Email')

    # enter invalid email
    def test_invalid_email(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@.com')
        function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        invalid_mail_alert = function.driver.find_element(By.XPATH, "//div[@type='invalid']").text
        assert (invalid_mail_alert == 'email must be a valid email')

    # correct email and invalid password
    def test_invalid_password(self, get_data):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys(get_data.email)
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(get_data.invalid_password)
        function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(6)
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").clear()
        time.sleep(4)
        function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").clear()
        time.sleep(4)
        invalid_password_alert = function.driver.find_element(By.XPATH, "//div[@role='alert']").text
        assert (invalid_password_alert == 'Invalid credentials')