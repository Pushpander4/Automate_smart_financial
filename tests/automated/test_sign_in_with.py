import time

from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()
def testtext_of_sign_in_with():
    text_of_sign_in_with = funtion.driver.find_element(By.XPATH,"//h5[normalize-space()='Sign in with']").text
    assert (text_of_sign_in_with == "Sign in with")


