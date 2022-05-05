import time

from Automation import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()
funtion.driver.implicitly_wait(5)

#when no details are entered for sign up . checking waring message
#(Working)
def test_click_signup():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()

def test_click_button_register():
    funtion.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()

def test_please_enter_you_first_name():
    please_enter_you_first_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your first name']").text
    assert please_enter_you_first_name == 'Please enter your first name'


def test_please_enter_your_last_name():
    please_enter_your_last_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your last name']").text
    assert please_enter_your_last_name == 'Please enter your last name'


def test_please_select_a_time_zone():
    please_select_a_time_zone = funtion.driver.find_element(By.XPATH, "//span[normalize-space()='Please select a time zone']").text
    assert please_select_a_time_zone == 'Please select a time zone'


def test_please_enter_your_address():
    please_enter_your_address = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your address']").text
    assert please_enter_your_address == 'Please enter your address'


def test_please_enter_your_city():
    please_enter_your_city = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your city']").text
    assert please_enter_your_city == 'Please enter your city'


def test_Please_enter_your_state():
    please_enter_your_city = funtion.driver.find_element(By.XPATH, "//span[normalize-space()='Please select your state']").text
    assert please_enter_your_city == 'Please select your state'


def test_Please_enter_your_zip():
    please_enter_your_zip = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your zip']").text
    assert please_enter_your_zip == 'Please enter your zip'


def test_Please_enter_a_valid_email():
    please_enter_a_valid_email = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter a valid email']").text
    assert please_enter_a_valid_email == 'Please enter a valid email'


def test_Please_enter_your_password():
    Please_enter_your_password = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your password']").text
    assert Please_enter_your_password == 'Please enter your password'



#try to  signup with already taken email
#working
time.sleep(2)
def test_enter_signup_details():
    funtion.driver.refresh()
    funtion.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
    funtion.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("XYZ")
    funtion.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("2345672347")
    funtion.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fgdwbhgbgibgibgjgjdjgad djgndgijjndgjsdn")
    funtion.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("chicago")
    funtion.driver.find_element(By.XPATH, "//div[@class='col-xl-6']//div[@class='select2-selection__control css-yk16xz-control']").click()
    funtion.driver.find_element(By.ID, "react-select-2-option-0-5").click()
    time.sleep(6)
    funtion.driver.find_element(By.XPATH, "//div[@class='col-xl-3']//div[@class='select2-selection__value-container select2-selection__value-container--has-value css-1hwfws3']").click()
    funtion.driver.find_element(By.ID, "react-select-3-option-0-1").click()
    funtion.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    funtion.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12345")
    funtion.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("piyush@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Abcderfgh1@")
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()
    time.sleep(2)

def test_email_has_already_been_take():
    logo = funtion.driver.find_element(By.XPATH, "//div[@class='text-center p-4']//img")
    funtion.driver.execute_script("arguments[0].scrollIntoView()", logo)
    time.sleep(2)
    email_has_already_been_take = funtion.driver.find_element(By.XPATH, "//div[@role = 'alert']").text
    assert email_has_already_been_take == 'email has already been taken'



#user should not able to sign up with invalid email ID
#working
def test_user_should_not_able_to_signup_in_with_in_valid_email():
    funtion.driver.refresh()
    funtion.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
    funtion.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("XYZ")
    funtion.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("2345672347")
    funtion.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fgdwbhgbgibgibgjgjdjgad djgndgijjndgjsdn")
    funtion.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Delhi")
    funtion.driver.find_element(By.XPATH, "//div[@class='col-xl-6']//div[@class='select2-selection__control css-yk16xz-control']").click()
    funtion.driver.find_element(By.ID, "react-select-2-option-0-5").click()
    time.sleep(6)
    funtion.driver.find_element(By.XPATH, "//div[@class='col-xl-3']//div[@class='select2-selection__value-"
                                          "container select2-selection__value-container--has-value css-1hwfws3']").click()
    funtion.driver.find_element(By.ID, "react-select-3-option-0-1").click()
    funtion.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    funtion.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12345")
    funtion.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("piyushikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Abcderfgh1@")
    email_must_be_a_valid_email = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='email must be a valid email']").text
    assert email_must_be_a_valid_email == 'email must be a valid email'

#warning in first name and last name for more then 2 char and in address 3 char.
#first_name_must_be_at_least_2_characters
def test_first_name_and_last_name_for_more_then_2_har_and_in_address_3_char():
    funtion.driver.refresh()
    funtion.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("A")
    funtion.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("X")
    funtion.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fg")


def test_first_name_must_be_at_least_2_characters():
    first_name_must_be_at_least_2_characters = funtion.driver.find_element(By.XPATH,
                                                                           "//div[normalize-space()='first_name must be at least 2 characters']").text
    assert first_name_must_be_at_least_2_characters == 'first_name must be at least 2 characters'


def test_last_name_must_be_at_least_2_characters():
    last_name_must_be_at_least_2_characters = funtion.driver.find_element(By.XPATH,
                                                                          "//div[normalize-space()='last_name must be at least 2 characters']").text
    assert last_name_must_be_at_least_2_characters == 'last_name must be at least 2 characters'


#not_able_to_sign_up_with_invalid_zip
def test_not_able_to_sign_up_with_invalid_zip():
    funtion.driver.refresh()
    funtion.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12")
    funtion.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
    funtion.driver.back()