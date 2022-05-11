import time

import pytest

from Automation import function
from selenium.webdriver.common.by import By


function.open_browser()
function.driver.implicitly_wait(5)

# when no details are entered for sign up . checking warning message
class TestInvalidSenarios:
    def test_click_signup(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()

    def test_click_button_register(self):
        function.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()

    def test_please_enter_you_first_name(self):
        please_enter_you_first_name = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your first name']").text
        assert please_enter_you_first_name == 'Please enter your first name'

    @pytest.mark.skip(reason="This Functionality is noy yet implemented (Please enter your last name)")
    def test_please_enter_your_last_name(self):
        please_enter_your_last_name = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your last name']").text
        assert please_enter_your_last_name == 'Please enter your last name'


    def test_please_select_a_time_zone(self):
        please_select_a_time_zone = function.driver.find_element(By.XPATH, "//span[normalize-space()='Please select a time zone']").text
        assert please_select_a_time_zone == 'Please select a time zone'

    def test_please_enter_your_address(self):
        please_enter_your_address = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your address']").text
        assert please_enter_your_address == 'Please enter your address'

    def test_please_enter_your_city(self):
        please_enter_your_city = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your city']").text
        assert please_enter_your_city == 'Please enter your city'

    def test_Please_enter_your_state(self):
        please_enter_your_city = function.driver.find_element(By.XPATH, "//span[normalize-space()='Please select your state']").text
        assert please_enter_your_city == 'Please select your state'

    def test_Please_enter_your_zip(self):
        please_enter_your_zip = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your zip']").text
        assert please_enter_your_zip == 'Please enter your zip'

    def test_Please_enter_a_valid_email(self):
        please_enter_a_valid_email = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter a valid email']").text
        assert please_enter_a_valid_email == 'Please enter a valid email'

    def test_Please_enter_your_password(self):
        Please_enter_your_password = function.driver.find_element(By.XPATH, "//div[normalize-space()='Please enter your password']").text
        assert Please_enter_your_password == 'Please enter your password'


    # try to  signup with already taken email

    time.sleep(2)
    def test_enter_signup_details(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("XYZ")
        function.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("2345672347")
        function.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fgdwbhgbgibgibgjgjdjgad djgndgijjndgjsdn")
        function.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("chicago")
        function.driver.find_element(By.XPATH, "//div[@class='col-xl-6']//div[@class='select2-selection__control css-yk16xz-control']").click()
        function.driver.find_element(By.ID, "react-select-2-option-0-5").click()
        time.sleep(6)
        function.driver.find_element(By.XPATH, "//div[@class='col-xl-3']//div[@class='select2-selection__value-container select2-selection__value-container--has-value css-1hwfws3']").click()
        function.driver.find_element(By.ID, "react-select-3-option-0-1").click()
        function.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        function.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12345")
        function.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("piyush@ikshalabs.com")
        function.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Abcderfgh1@")
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Create New Account']").click()
        time.sleep(2)

    def test_email_has_already_been_take(self):
        logo = function.driver.find_element(By.XPATH, "//div[@class='text-center p-4']//img")
        function.driver.execute_script("arguments[0].scrollIntoView()", logo)
        time.sleep(2)
        email_has_already_been_take = function.driver.find_element(By.XPATH, "//div[@role = 'alert']").text
        assert email_has_already_been_take == 'email has already been taken'

    # user should not able to sign up with invalid email ID

    def test_user_should_not_able_to_log_in_with_in_valid_email(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("XYZ")
        function.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("2345672347")
        function.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fgdwbhgbgibgibgjgjdjgad djgndgijjndgjsdn")
        function.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Delhi")
        function.driver.find_element(By.XPATH, "//div[@class='col-xl-6']//div[@class='select2-selection__control css-yk16xz-control']").click()
        function.driver.find_element(By.ID, "react-select-2-option-0-5").click()
        time.sleep(6)
        function.driver.find_element(By.XPATH, "//div[@class='col-xl-3']//div[@class='select2-selection__value-"
                                              "container select2-selection__value-container--has-value css-1hwfws3']").click()
        function.driver.find_element(By.ID, "react-select-3-option-0-1").click()
        function.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        function.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12345")
        function.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("piyushikshalabs.com")
        function.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Abcderfgh1@")
        email_must_be_a_valid_email = function.driver.find_element(By.XPATH, "//div[normalize-space()='email must be a valid email']").text
        assert email_must_be_a_valid_email == 'email must be a valid email'

    # warning in first name and last name for more then 2 char and in address 3 char.
    # first_name_must_be_at_least_2_characters
    #TODO:Create different funtions for all
    def test_first_name_last_name_should_have_more_then_2_char_and_in_address_3_char(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("A")
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("X")
        function.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("fg")

    def test_first_name_must_be_at_least_2_characters(self):
        first_name_must_be_at_least_2_characters = function.driver.find_element(By.XPATH,
                                                                               "//div[normalize-space()='first_name must be at least 2 characters']").text
        assert first_name_must_be_at_least_2_characters == 'first_name must be at least 2 characters'

    @pytest.mark.skip(reason="This Functionality is noy yet implemented (last_name must be at least 2 characters)")
    def test_last_name_must_be_at_least_2_characters(self):
        last_name_must_be_at_least_2_characters = function.driver.find_element(By.XPATH,
                                                                              "//div[normalize-space()='last_name must be at least 2 characters']").text
        assert last_name_must_be_at_least_2_characters == 'last_name must be at least 2 characters'

    # not_able_to_sign_up_with_invalid_zip
    def test_not_able_to_sign_up_with_invalid_zip(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//input[@name='zip_code']").send_keys("12")
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("ABC")
        function.driver.back()