import time
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest


funtion.open_browser()
@pytest.mark.usefixtures("get_Data")
#when both fields (email and name are empty) and log in button is clicked.
class Test_Invalid_Login():
    def test_Click_login(self):

        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)


    def test_please_enter_your_email(self):
        email_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
        assert (email_alert == 'Please Enter Your Email')


    def test_please_enter_your_password(self):
        password_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
        assert (password_alert == 'Please Enter Your Password')

    #enter email , don't enter password and log in button is clicked.
    def test_enter_email_not_password(self):
        funtion.driver.refresh()
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@ikshalabs.com')
        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        password_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
        assert (password_alert == 'Please Enter Your Password')
        time.sleep(2)
    #enter password , don't enter email and log in button is clicked.
    def test_enter_password_not_email(self):
        funtion.driver.refresh()
        time.sleep(3)
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@123")
        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        email_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
        assert (email_alert == 'Please Enter Your Email')


    #enter invalid email
    def test_invalid_email(self):
        funtion.driver.refresh()
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@.com')
        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        invalid_mail_alert = funtion.driver.find_element(By.XPATH, "//div[@type='invalid']").text
        assert (invalid_mail_alert == 'email must be a valid email')


    #correct email and invalid password
    def test_invalid_password(self,get_Data):
        funtion.driver.refresh()
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys(get_Data[0])
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(get_Data[1])
        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(6)
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").clear()
        time.sleep(4)
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").clear()
        time.sleep(4)
        invalid_password_alert = funtion.driver.find_element(By.XPATH, "//div[@role='alert']").text
        assert (invalid_password_alert == 'Invalid credentials')
