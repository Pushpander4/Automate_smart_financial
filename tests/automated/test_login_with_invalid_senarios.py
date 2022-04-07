import time
from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()


def testClick_login():
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

# def test_please_enter_your_email():
#     email_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Email']").text
#     assert (email_alert == 'Please Enter Your Email')
#
# def test_please_enter_your_password():
#     password_alert = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Password']").text
#     assert (password_alert == 'Please Enter Your Password')


def test_invalid_email():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('piyush@.com')
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    invalid_mail_alert = funtion.driver.find_element(By.XPATH, "//div[@type='invalid']").text
    assert (invalid_mail_alert == 'email must be a valid email')
    time.sleep(4)



# def test_invalid_password():
#
#     funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys('piyush@123')
#     time.sleep(8)
#     funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#     time.sleep(8)
#     invalid_password_alert = funtion.driver.find_element(By.XPATH, "//div[@role='alert']").text
#     time.sleep(10)
#     assert (invalid_password_alert == 'Invalid credentials')
#     time.sleep(8)