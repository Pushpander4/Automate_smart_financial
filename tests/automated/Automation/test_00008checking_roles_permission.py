import time
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest

funtion.driver.implicitly_wait(5)
@pytest.mark.usefixtures("tc_setup")
class Test_check_roles:

    def test_check_roles_edit(self):

#checking role creation
        funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
        funtion.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys("Team member 27")
        funtion.driver.find_element(By.ID, "1-switch-group-Role").click()
        save_button = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        funtion.driver.execute_script("arguments[0].scrollIntoView()", save_button)
        time.sleep(1)
#click save button
        funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)

        card_elements = funtion.driver.find_elements(By.CLASS_NAME, "card")
        for card_elem in card_elements:
            try:
                title_elem = card_elem.find_element(By.CLASS_NAME, "text-dark")
                if title_elem.text == "Team member 27":
                    card_elem.find_element(By.CLASS_NAME, "btn-sfpink").click()
            except Exception as e:
                print(e)

        # Main toggle button of ROLE
        """
         After main ROLE button is ON , All sub button should get ON.

         Roles        = ON
         Create Role  = ON
         Read Role    = ON
         Update Roles = ON
         Delete Roles = ON
         """

    def test_check_roles_1(self):


        parent_role = funtion.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
        create_role = funtion.driver.find_element(By.ID , "1-switch-item-can_create").is_selected()
        read_role = funtion.driver.find_element(By.ID, "1-switch-item-can_read").is_selected()
        update_role = funtion.driver.find_element(By.ID, "1-switch-item-can_update").is_selected()
        delete_role = funtion.driver.find_element(By.ID, "1-switch-item-can_delete").is_selected()
        print(parent_role)
        print(create_role)
        print(read_role)
        print(update_role)
        print(delete_role)

        # When in ROLE'S  one of the sub button is off(then role main toggle buttonn should get off)
        """

         After one sub button is OFF , Roles main button should get OFF
         Roles        = ON
         Create Role  = OFF
         Read Role    = ON
         Update Roles = ON
         Delete Roles = ON
         """

    def test_check_roles_2(self):

            funtion.driver.find_element(By.ID, "1-switch-item-can_read").click()
            time.sleep(2)
            roles = funtion.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
            time.sleep(2)
            assert roles == False

            # When in ROLE'S, all 4 sub button are on(then role main toggle button should get on)
            """
            After all 4 sub button are ON , 'ROLES' automatically get ON

            Roles        = OFF
            Create Role  = ON
            Read Role    = ON
            Update Roles = ON
            Delete Roles = ON
            """

    def test_check_roles_3(self):

        funtion.driver.find_element(By.ID, "1-switch-item-can_read").click()
        time.sleep(3)
        roles2=funtion.driver.find_element(By.ID, "1-switch-group-Role").is_selected()
        assert roles2 == True


    """
    same logic is applicable for Campaign and membership
    """
