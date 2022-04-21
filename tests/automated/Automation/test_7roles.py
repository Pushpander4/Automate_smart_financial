
import time
from Automation import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()
funtion.driver.implicitly_wait(5)
#checking role creation
def test_login():
    funtion.driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys("pushpander@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("smartfinancial")
    text_on_login_button = funtion.driver.find_element(By.XPATH,"//button[@type='submit']").text
    assert (text_on_login_button == "Log In")
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

def test_organization():
    text_on_organization = funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").text
    assert (text_on_organization == "Organization")
    funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()

def test_roles():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
    text_on_roles = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").text
    assert (text_on_roles == "Roles")
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()

def test_create_new_role():
    text_create_new_role = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").text
    assert (text_create_new_role == "Create New Role")
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
#enter the role name
    funtion.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys("anuj")
#select All toggle button (role, campaign ,membership)
    funtion.driver.find_element(By.XPATH, "//input[@id='1']").click()
    funtion.driver.find_element(By.XPATH, "//input[@id='2']").click()
    save_button = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    funtion.driver.execute_script("arguments[0].scrollIntoView()", save_button)
    time.sleep(1)
    funtion.driver.find_element(By.XPATH, "//input[@id='4']").click()

#click save button
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(5)

    copy_ss = funtion.driver.find_element(By.XPATH, "//div[@class='text-sm-end d-none d-sm-block']")
    funtion.driver.execute_script("arguments[0].scrollIntoView()", copy_ss)



def test_abc():
     card_elements = funtion.driver.find_elements(By.CLASS_NAME, "card")
     for card_elem in card_elements:
         try:
             title_elem = card_elem.find_element(By.CLASS_NAME, "text-dark")
             if title_elem.text == "anuj":
                card_elem.find_element(By.CLASS_NAME,"btn-sfpink").click()
         except Exception as e:
             print(e)






