import time

from automated import funtion
import time
from selenium.webdriver.common.by import By

funtion.open_browser()


def testWelcometext():
    welcome_back_text=funtion.driver.find_element(By.XPATH ,"//h5[normalize-space()='Welcome Back !']").text
    assert ( welcome_back_text == "Welcome Back !")

def testSign_in_to_continue_to_Smart_Financial():
    text_sign_in_ign_in_to_continue_to_Smart_Financial = funtion.driver.find_element(By.XPATH ,"//p[normalize-space()='Sign in to continue to Smart Financial']").text
    assert (text_sign_in_ign_in_to_continue_to_Smart_Financial == "Sign in to continue to Smart Financial")

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


def testlogin():
    time.sleep(10)
    funtion.login()
