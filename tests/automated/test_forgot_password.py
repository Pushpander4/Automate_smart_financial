from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()
def testtext_of_forgot_password():
    text_of_sign_in_with = funtion.driver.find_element(By.XPATH,"//a[normalize-space()='Forgot your password?']").text
    assert (text_of_sign_in_with == "Forgot your password?")


# def testclick_forgot_password():
#     funtion.driver.find_element(By.XPATH,"//a[normalize-space()='Forgot your password?']").click()

def testIn_forgot_password_email():
    text_of_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
    assert (text_of_email == "Email")

def testtext_2022_Smart_Financial():
    t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 Smart Financial']").text
    assert (t_2022_Smart_Financial == "© 2022 Smart Financial")

def testIn_email_place_holder():
    place_holder_on_email_place_holder = funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").get_attribute("placeholder")
    assert (place_holder_on_email_place_holder == "Enter email")
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("sheerin@example.com")


# def testtext_on_reset_button():
#     text_on_reset_button = funtion.driver.find_element(By.XPATH,"//button[normalize-space()='Reset']").text
#     assert (text_on_reset_button == "Reset")
#     funtion.driver.find_element(By.XPATH,"//button[normalize-space()='Reset']").click()

# def testReset_link_text():
#     text_on_Reset_link_text = funtion.driver.find_element(By.XPATH,"//div[@role='alert']").text
#     assert (text_on_Reset_link_text == "Reset link are sended to your mailbox, check there first")




