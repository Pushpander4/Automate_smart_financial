import time
from automated import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


# TODO: add a test for checking smartfinancial title image 

def testemail():
    text_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
    assert (text_email == "Email")


def testpassword():
    text_password = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Password']").text
    assert (text_password == "Password")

def testremember_me_text():
    text_on_remember = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Remember me']").text
    assert (text_on_remember == "Remember me")

def testremember_me():
    funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").click()
    v1 = funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_selected()
    assert (v1 == True)




time.sleep(4)

def testlogin():
    time.sleep(4)
    funtion.login()
