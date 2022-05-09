import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest
import random


function.open_browser()
function.driver.implicitly_wait(5)
#checking role creation
time.sleep(5)


@pytest.mark.usefixtures("tc_setup")
class TestRoles:
    def test_organization_present_in_sidebar(self):
        time.sleep(5)
        text_on_organization = function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").text
        assert text_on_organization == "Organization" , 'Organization spelling incorrect'
        function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()

    def test_roles_present_in_sidebar(self):
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        text_on_roles = function.driver.find_element(By.XPATH,
                                                     "//a[normalize-space()='Roles']").text
        assert text_on_roles == "Roles"
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()


    def test_create_new_role(self):
        role_number_suffix = random.randint(100000, 999999)
        role_name = "Team member " + str(role_number_suffix)
        text_create_new_role = function.driver.find_element(By.XPATH,
                                                           "//a[normalize-space()='Create New Role']").text
        assert text_create_new_role == "Create New Role"
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
        # enter the role name
        function.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys(role_name)
        # select All toggle button (role, campaign ,membership)
        function.driver.find_element(By.ID, "1-switch-item-can_create").click()
        function.driver.find_element(By.ID, "2-switch-group-Campaign").click()
        save_button = function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        function.driver.execute_script("arguments[0].scrollIntoView()", save_button)
        time.sleep(1)
        function.driver.find_element(By.ID, "4-switch-group-Membership").click()

        # click save button
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)

        copy_ss = function.driver.find_element(By.XPATH, "//div[@class='text-sm-end d-none d-sm-block']")
        function.driver.execute_script("arguments[0].scrollIntoView()", copy_ss)
        card_elements = function.driver.find_elements(By.CLASS_NAME, "card")
        for card_elem in card_elements:
            try:
                title_elem = card_elem.find_element(By.XPATH, "//a[@class='text-dark']")
                if title_elem.text == role_name:
                    card_elem.find_element(By.XPATH, "//button[@class='btn btn-sfpink btn btn-secondary']").click()
            except Exception as e:
                print(e)

        function.driver.back()

    """
    creating new role without giving any permission to the user
    """
    def test_new_role_without_any_permission(self):
        #function.driver.back()

# click on new role creation button
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
        function.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys("New user without any permission")

        save_button = function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        function.driver.execute_script("arguments[0].scrollIntoView()", save_button)
        time.sleep(4)
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(4)

    # def test_log_out(self):
    #     function.driver.find_element(By.XPATH, "//img[@alt='Header Avatar']").click()
    #     function.driver.find_element(By.XPATH, "//a[@href='/logout']").click()





