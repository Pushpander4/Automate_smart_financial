# from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Automation import function
from selenium.webdriver.common.by import By
import pytest


class TestSignup:

    def test_signup_enable_or_not(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").is_enabled()

    def test_signup_text(self):
        text_on_signup = function.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").text
        assert text_on_signup == "Signup now"

    def test_click_signup(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()
        time.sleep(5)

    def testEnter_first_name_enable(self):
        function.driver.find_element(By.XPATH, "//label[normalize-space()='First Name']").is_enabled()

    def testEnter_first_name(self):
        Enter_first_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='First Name']").text
        assert Enter_first_name == "First Name"

    def testEnter_Last_name_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").is_enabled()

    def testEnter_last_name(self):
        Enter_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Last Name']").text
        assert Enter_last_name == "Last Name"

    def testEnter_phone_number_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='phone_num']").is_enabled()

    def testEnter_phone_number(self):
        Enter_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Phone']").text
        assert Enter_last_name == "Phone"

    def testEnter_timezone_enable(self):
        function.driver.find_element(By.CLASS_NAME, "css-8mmkcg").is_enabled()

    def testEnter_timezone(self):
        Enter_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Timezone']").text
        assert Enter_last_name == "Timezone"

    def testEnter_address_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='address']").is_enabled()

    def testEnter_address(self):
        enter_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Address']").text
        assert enter_last_name == "Address"

    def test_enter_city_enable(self):
        function.driver.find_element(By.ID, "react-select-3-input").is_enabled()

    def test_enter_city_text(self):
        city_text = function.driver.find_element(By.XPATH, "//label[normalize-space()='City']").text
        assert city_text == "City"

    def test_enter_state_text(self):
        state_text = function.driver.find_element(By.XPATH, "//label[normalize-space()='State']").text
        assert  state_text == "State"

    def test_enter_zipcode_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='zip_code']").is_enabled()

    def test_enter_zipcode(self):
        enter_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Zip Code']").text
        assert enter_last_name == "Zip Code"

    def test_enter_email_place_enable(self):
        function.driver.find_element(By.XPATH, "//input[@id='email']").is_enabled()

    def test_enter_email_place(self):
        enter_email_place = function.driver.find_element(By.XPATH, "//label[normalize-space()='Email']").text
        assert enter_email_place == "Email"

    def test_enter_Password_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='password']").is_enabled()

    def test_enter_password(self):
        enter_password = function.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").text
        assert enter_password == "Password"

    def test_text_on_button_register(self):
        text_on_button_register = function.driver.find_element(
            By.XPATH,"//button[normalize-space()='Create New Account']").text
        assert text_on_button_register == "Create New Account"

    def test_click_button_register_enable(self):
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").is_enabled()
        logo = function.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']")
        function.driver.execute_script("arguments[0].scrollIntoView()", logo)

    def test_click_button_register(self):
        time.sleep(3)
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()

    def test_text_by_registering_you_agree_to_the(self):
        text_by_registering_you_agree_to_the = function.driver.find_element(By.XPATH, "//p[@class='mb-0']").text
        assert text_by_registering_you_agree_to_the == "By registering you agree to the Terms of Use"

    def test_text_click_terms_of_use(self):
        text_click_terms_of_use = function.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").text
        assert text_click_terms_of_use == "Terms of Use"

    def test_terms_of_use_enable(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").is_enabled()
        time.sleep(3)

    @pytest.mark.xfail(reason="This functionality is not yet implemented")
    def test_click_terms_of_use(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").click()

    def test_already_have_an_account(self):
        t_already_have_an_account = function.driver.find_element(
            By.CSS_SELECTOR, "div[class='mt-5 text-center'] p:nth-child(1)").text
        assert t_already_have_an_account == "Already have an account ? Login"

    def test_back_to_login(self):
        text_on_login_back = function.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
        assert text_on_login_back == "Login"

    def test_login_button_to_go_back_to_login_page_enable(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").is_enabled()

    def test_text_2022_Smart_Financial(self):
        t_2022_Smart_Financial = function.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 SmartFinancial']").text
        assert t_2022_Smart_Financial == "© 2022 SmartFinancial"

    def test_click_on_login_button_to_go_back_to_login_page(self):
        back_to_login_text = function.driver.find_element(By.LINK_TEXT, "Login")
        function.driver.execute_script("arguments[0].scrollIntoView()", back_to_login_text)
        function.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(4)
        wait = WebDriverWait(function.driver, 10)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
