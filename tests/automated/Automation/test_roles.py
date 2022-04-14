import time
from Automation import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()
funtion.driver.implicitly_wait(5)
#checking role creation
def test_login():
    funtion.driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys("piyush@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@1234")

def test_login_button_text():
    text_on_login_button = funtion.driver.find_element(By.XPATH,"//button[@type='submit']").text
    assert (text_on_login_button == "Log In")
def test_login_button():
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

def test_organization():
    text_on_organization = funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").text
    assert (text_on_organization == "Organization")
    funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
def test_roles():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
    text_on_roles = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").text
    assert (text_on_roles == "Roles")
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()

def test_logout():
    funtion.driver.find_element(By.XPATH, "//img[@alt='Header Avatar']").click()
    funtion.driver.find_element(By.XPATH, "//span[normalize-space()='Logout']").click()



