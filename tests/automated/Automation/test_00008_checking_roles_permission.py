import time
from Automation import function
from selenium.webdriver.common.by import By
import random
import pytest

function.open_browser()
function.driver.implicitly_wait(5)


@pytest.mark.usefixtures("tc_setup")
class TestCheckRoles:
    def test_setup_create_blank_role(self):
        role_number_suffix = random.randint(100000, 999999)
        role_name = "Team member " + str(role_number_suffix)

        function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
        function.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys(role_name)
        # function.driver.find_element(By.ID, "1-switch-group-Role").click()
        save_button = function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        function.driver.execute_script("arguments[0].scrollIntoView()", save_button)
        time.sleep(3)
        # click save button
        function.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)

        card_elements = function.driver.find_elements(By.XPATH, "//div[@class='card']")
        for card_elem in card_elements:
            try:
                title_elem = card_elem.find_element(By.XPATH, "//a[@class='text-dark']")
                if title_elem.text == role_name:
                    card_elem.find_element(By.XPATH, "//button[@class='btn btn-sfpink btn btn-secondary']").click()
            except Exception as e:
                print(e)

    """
    Main toggle button of ROLE
        After main ROLE button is ON , All sub button should get ON.
        Roles        = ON
        Create Role  = ON
        Read Role    = ON
        Update Roles = ON
        Delete Roles = ON
    """

    def test_parent_button_toggle_children(self):
        function.driver.find_element(By.ID, "1-switch-group-Role").click()
        time.sleep(2)
        function.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
        function.driver.find_element(By.ID, "1-switch-item-can_create").is_selected()
        function.driver.find_element(By.ID, "1-switch-item-can_read").is_selected()
        function.driver.find_element(By.ID, "1-switch-item-can_update").is_selected()
        function.driver.find_element(By.ID, "1-switch-item-can_delete").is_selected()


    """
    When in ROLE'S  one of the sub button is off(then role main toggle button should get off)
    
    After one sub button is OFF , Roles main button should get OFF
         Roles        = ON
         Create Role  = OFF
         Read Role    = ON
         Update Roles = ON
         Delete Roles = ON
    """
    def test_child_button_off_turns_parent_button_off(self):
        function.driver.find_element(By.ID, "1-switch-item-can_delete").click()
        time.sleep(2)
        roles = function.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
        assert roles == False


    """
     When in ROLE'S, all 4 sub button are on(then role main toggle button should get on)

    After all 4 sub button are ON , 'ROLES' automatically get ON
        Roles        = OFF
        Create Role  = ON
        Read Role    = ON
        Update Roles = ON
        Delete Roles = ON
    """

    def test_all_child_button_on_turns_parent_button_on(self):
        function.driver.find_element(By.ID, "1-switch-item-can_delete").click()
        time.sleep(3)
        roles = function.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
        assert roles == True

    """
    same logic is applicable for Campaign and membership
    """


    def test_log_out(self):
        function.driver.find_element(By.XPATH, "//img[@alt='Header Avatar']").click()
        function.driver.find_element(By.XPATH, "//a[@href='/logout']").click()


