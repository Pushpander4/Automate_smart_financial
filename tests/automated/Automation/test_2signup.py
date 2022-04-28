# from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest

funtion.open_browser()

class TestSignup:

     def test_signup_enable_or_not(self):
         funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").is_enabled()


     def test_signup_text(self):
         text_on_signup = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").text
         assert (text_on_signup == "Signup now")


     def testClick_signup(self):
         funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()
         time.sleep(5)


     def testEnter_first_name_enable(self):

         funtion.driver.find_element(By.XPATH, "//label[normalize-space()='First Name']").is_enabled()


    def testEnter_first_name():
        Enter_first_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='First Name']").text
        assert (Enter_first_name == "First Name")
        # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
        # print(text_name)


    def testEnter_Last_name_enable():
        funtion.driver.find_element(By.XPATH, "//input[@name='last_name']").is_enabled()


    def testEnter_last_name():
         Enter_last_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Last Name']").text
         assert (Enter_last_name == "Last Name")
         # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
         # print(text_name)


    def testEnter_phone_number_enable():
         funtion.driver.find_element(By.XPATH, "//input[@name='phone']").is_enabled()


    def testEnter_phone_number():
        Enter_last_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Phone']").text
        assert (Enter_last_name == "Phone")
        # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
        # print(text_name)


    def testEnter_timezone_enable():
        funtion.driver.find_element(By.CLASS_NAME, "css-8mmkcg").is_enabled()


    def testEnter_timezone():
         Enter_last_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Timezone']").text
         assert (Enter_last_name == "Timezone")


    def testEnter_address_enable():
        funtion.driver.find_element(By.XPATH, "//input[@name='address']").is_enabled()


    def testEnter_Address():
         Enter_last_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Address']").text
         assert (Enter_last_name == "Address")
         # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
         # print(text_name)


    def testEnter_city_enable():
         funtion.driver.find_element(By.ID, "react-select-3-input").is_enabled()


    def testEnter_city_text():
         city_text = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='City']").text
         assert (city_text == "City")

    def testEnter_state_text():
        state_text = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='State']").text
        assert (state_text == "State")
    def testEnter_zipcode_enable():
         funtion.driver.find_element(By.XPATH, "//input[@name='zip_code']").is_enabled()

    def testEnter_zipcode():
         Enter_last_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Zip Code']").text
         assert (Enter_last_name == "Zip Code")
         # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
         # print(text_name)


def testEnter_email_place_enable():
    funtion.driver.find_element(By.XPATH, "//input[@id='email']").is_enabled()


# def testEnter_email_place_holder():
#     Enter_email_place_holder = funtion.driver.find_element(By.XPATH, "//input[@id='email']").get_attribute("placeholder")
#     assert (Enter_email_place_holder == "Enter email")


def testEnter_email_place():
    Enter_email_place = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Email']").text
    assert (Enter_email_place == "Email")


def test_Enter_Password_enable():
    funtion.driver.find_element(By.XPATH, "//input[@name='password']").is_enabled()


# def testplace_holder_Enter_Password():
#     place_holder_Enter_Password = funtion.driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']").get_attribute("placeholder")
#     assert (place_holder_Enter_Password == "Enter Password")


def testEnter_Password():
    Enter_Password = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").text
    assert (Enter_Password == "Password")


def test_text_on_button_register():
    text_on_button_register = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").text
    assert (text_on_button_register == "Create New Account")


def test_click_button_register_enable():
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").is_enabled()
    logo = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']")
    funtion.driver.execute_script("arguments[0].scrollIntoView()", logo)


def test_click_button_register():
    time.sleep(3)
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()


def test_text_by_registering_you_agree_to_the():
    text_by_registering_you_agree_to_the = funtion.driver.find_element(By.XPATH, "//p[@class='mb-0']").text

    assert (text_by_registering_you_agree_to_the == "By registering you agree to the Terms of Use")


def test_text_click_terms_of_use():
    text_click_terms_of_use = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").text
    assert (text_click_terms_of_use == "Terms of Use")


def test_terms_of_use_enable():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").is_enabled()

time.sleep(3)
@pytest.mark.xfail  # Functionality is not yet implemented.
def test_click_terms_of_use():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").click()


def test_already_have_an_account():
    t_already_have_an_account = funtion.driver.find_element(By.CSS_SELECTOR,
                                                            "div[class='mt-5 text-center'] p:nth-child(1)").text
    assert (t_already_have_an_account == "Already have an account ? Login")
def testbacktologin():
    text_on_login_back = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
    assert (text_on_login_back == "Login")
def test_login_button_to_go_back_to_login_page_enable():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").is_enabled()

def testtext_2022_Smart_Financial():
    t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,
                                                         "//p[normalize-space()='© 2022 SmartFinancial']").text
    assert (t_2022_Smart_Financial == "© 2022 SmartFinancial")


def test_back_to_login():
    text_on_login_back = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
    assert (text_on_login_back == "Login")

def test_click_on_login_button_to_go_back_to_login_page():
    back_to_login_text = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
    funtion.driver.execute_script("arguments[0].scrollIntoView()",back_to_login_text)
    time.sleep(3)
    wait = WebDriverWait(funtion.driver, 10)
    wait.until(EC.element_to_be_clickable(back_to_login_text)).click()



