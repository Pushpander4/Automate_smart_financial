import time
from Automation import function
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest


function.open_browser()
# User management fields test
@pytest.mark.usefixtures('tc_setup')
class TestUserManagement:
    def test_UM_present_in_sidebar(self):
        function.driver.implicitly_wait(5)
        function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
        wait = WebDriverWait(function.driver, 2)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[normalize-space()='User Management']")))
        function.driver.find_element(By.XPATH, "//a[normalize-space()='User Management']").click()
        text_on_UM = function.driver.find_element(By.XPATH, "//a[normalize-space()='User Management']").text
        assert text_on_UM == "User Management"
        function.driver.find_element(By.XPATH, "//a[normalize-space()='User Management']").click()

    def test_text_roles_drop(self):
        text_role_drop = function.driver.find_element(By.XPATH, "//label[@class='form-label']").text
        assert text_role_drop == "Roles", "Value of text is not 'Roles'"

    @pytest.mark.skip
    def test_roles_drop_enable(self):
        function.driver.find_element(By.CLASS_NAME, "select2-selection__placeholder css-1wa3eu0-placeholder").is_enabled()

    def test_search(self):
        function.driver.find_element(By.ID, "search-bar-0").is_enabled()

    def test_text_add_user_button(self):
        time.sleep(2)
        text_button = function.driver.find_element(By.XPATH, "//button[normalize-space()='Add New User']").text
        assert text_button == "Add New User",  "Value of text is not 'Add New User'"

    def test_enabled_button_enable(self):
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Add New User']").is_enabled()

    def test_adduser_popup(self):
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Add New User']").click()
        time.sleep(7)
        text_adduser_popup = function.driver.find_element(By.ID, "myModalLabel").text
        assert text_adduser_popup == "Add New User"

    def test_text_first_name(self):
        time.sleep(5)
        text_first_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='First Name']").text
        assert text_first_name == "First Name"

    def test_first_name_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").is_enabled()

    def test_text_last_name(self):
        text_last_name = function.driver.find_element(By.XPATH, "//label[normalize-space()='Last Name']").text
        assert text_last_name == "Last Name"

    def test_last_name_enable(self):
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").is_enabled()

    def test_text_email_field(self):
        text_email = function.driver.find_element(By.XPATH, "//label[normalize-space()='Enter user email']").text
        assert text_email == "Enter user email"

    def test_email_field_enable(self):
        function.driver.find_element(By.XPATH, "//input[@placeholder='e.g. user@example.com']").is_enabled()

    def test_text_select_role(self):
        text_select_role = function.driver.find_element(By.XPATH, "//label[normalize-space()='Select Role']").text
        assert text_select_role == "Select Role"

    def test_select_role_enable(self):
        function.driver.find_element(By.XPATH, "//input[@placeholder='e.g. user@example.com']").is_enabled()

        """
        User management functionality test
        """

    @pytest.mark.skip(reason="This Functionality is not yet implemented(Bug)")
    def test_add_user(self, get_data):
        function.driver.implicitly_wait(5)
        function.driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys(get_data.first_name)
        print("User name added is " + get_data.first_name)
        function.driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys(get_data.last_name)
        function.driver.find_element(By.XPATH, "//input[@placeholder='e.g. user@example.com']").send_keys(get_data.email)


        #TODO:select roles
        #function.driver.find_element(By.XPATH, "//button[normalize-space()='Send Invite']").click()

    @pytest.mark.skip(reason="This function is skiped because test_add_user is skiped(dependent)")
    def test_edit_user(self):
        function.driver.implicitly_wait(5)
        function.driver.find_element(By.CLASS_NAME, "mdi mdi-pencil font-size-18").click()
        time.sleep(5)


    def test_log_out(self):
        function.driver.refresh()
        function.driver.find_element(By.XPATH, "//img[@alt='Header Avatar']").click()
        function.driver.find_element(By.XPATH, "//a[@href='/logout']").click()

