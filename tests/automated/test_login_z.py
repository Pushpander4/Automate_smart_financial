import time
from automated import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()


# TODO: add a test for checking smartfinancial title image

def test_smart_financial_title_image():
    funtion.driver.find_element(By.CSS_SELECTOR,".text-center.p-4").is_enabled()



def test_T1_email_input_field():
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").is_enabled()


def test_T2_password_input_field():
    funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").is_enabled()

def test_T3_email_text():
    text_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
    assert (text_email == "Email"), 'TEST-LOGIN-1 "Email" text should be present'


def test_T4_password_text():
    text_password = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Password']").text
    assert (text_password == "Password") , 'TEST-LOGIN-1 "Passsword" text should be present'

def test_remember_me_text():
    text_on_remember = funtion.driver.find_element(By.XPATH,"//label[@for='customControlInline']").text
    assert (text_on_remember == "Remember me")

def test_text_2022_Smart_Financial():
    t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 SmartFinancial']").text
    assert (t_2022_Smart_Financial == "© 2022 SmartFinancial")
def test_remember_me():
    funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_enabled()
    funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").click()
    v1 = funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_selected()
    assert (v1 == True)
    time.sleep(4)

def test_login():
    funtion.driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys("piyush@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@1234")
    time.sleep(5)

def test_login_button_text():
    text_on_login_button = funtion.driver.find_element(By.XPATH,"//button[@type='submit']").text
    assert (text_on_login_button == "Log In")



def test_login_button():
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()



def test_able_to_login():
    time.sleep(20)
    profile_page_url= (funtion.driver.current_url)
    assert (profile_page_url == "https://xenodochial-stonebraker-d239bd.netlify.app/profile")




