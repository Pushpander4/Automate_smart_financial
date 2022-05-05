import time
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest

funtion.open_browser()
funtion.driver.implicitly_wait(5)
#checking role creation
time.sleep(5)
@pytest.mark.usefixtures("tc_setup")
class Test_Roles_SF():

    def test_organization(self):
        time.sleep(5)

        text_on_organization = funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").text
        assert text_on_organization == "Organization"
        funtion.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()


    def test_roles(self):
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        text_on_roles = funtion.driver.find_element(By.XPATH,
                                                     "//a[normalize-space()='Roles']").text
        assert text_on_roles == "Roles"
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()


    def test_create_new_role(self):
        text_create_new_role = funtion.driver.find_element(By.XPATH,
                                                           "//a[normalize-space()='Create New Role']").text
        assert text_create_new_role == "Create New Role"
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
# enter the role name
        funtion.driver.find_element(By.XPATH, "//input[@name='role_name']").send_keys("Team member 10")
#select All toggle button (role, campaign ,membership)
        funtion.driver.find_element(By.ID, "1-switch-group-Role").click() # click on Role toggle button
        funtion.driver.find_element(By.ID, "2-switch-group-Campaign").click() # click on Campaign toggle button
        save_button = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        funtion.driver.execute_script("arguments[0].scrollIntoView()", save_button) # To scroll the page downwards
        time.sleep(1)
        funtion.driver.find_element(By.ID, "4-switch-group-Membership").click() #Click on membership toggle button

#click save button
        funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)

        copy_ss = funtion.driver.find_element(By.XPATH, "//div[@class='text-sm-end d-none d-sm-block']")
        funtion.driver.execute_script("arguments[0].scrollIntoView()", copy_ss)



    def test_click_on_edit_newly_created_role(self):
        card_elements = funtion.driver.find_elements(By.CLASS_NAME, "card")
        for card_elem in card_elements:
            try:
                title_elem = card_elem.find_element(By.Xpath, "//div[4]//div[1]//div[1]//h5[1]//a[1]")
                if title_elem.text == "Team member 10":
                    card_elem.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
            except Exception as e:
                print(e)







