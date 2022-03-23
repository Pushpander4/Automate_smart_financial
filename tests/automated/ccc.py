import time

from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()

def testClick_signup():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()

def test_checkplease_enter_ur_name():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email' and @aria-invalid='false']").send_keys("hi")
    time.sleep(5)
    a= funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email' and @aria-invalid='false']").get_attribute("value")
    print(a)
    assertIsNone  ( a, "The result is equal to none")




def test_click_button_register():
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()

