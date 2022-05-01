import time
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.usefixtures("tc_setup")
class check_roles:
    def test_check_roles_edit(self):

        funtion.open_browser()
        funtion.driver.implicitly_wait(5)
    #checking role creation
        funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
        funtion.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys("Team member 27")
        funtion.driver.find_element(By.XPATH, "//input[@id='1']").click()
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

        parent_role = funtion.driver.find_element(By.XPATH, "//input[@id='1']").is_selected()
        create_role = funtion.driver.find_element(By.XPATH , "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]").is_selected()
        read_role = funtion.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]").is_selected()
        update_role = funtion.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/input[1]").is_selected()
        delete_role = funtion.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/input[1]").is_selected()
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

            funtion.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]").click()
            time.sleep(2)
            roles = funtion.driver.find_element(By.XPATH, "//input[@id='1']").is_selected()
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

        funtion.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]").click()
        time.sleep(3)
        roles2=funtion.driver.find_element(By.XPATH, "//input[@id='1']").is_selected()
        assert roles2 == True


    """
    same logic is applicable for Campaign and membership
    """
