import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest

function.open_browser()
function.driver.implicitly_wait(5)
#checking role creation
time.sleep(5)
@pytest.mark.skip(reason="This Functionality is not yet implemented(role getting create without entering name")
def test_invalid_role_creation_senorios():
    pass
# @pytest.mark.usefixtures("tc_setup")
#
# class Test_Create_Role_Without_Name():
#     function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
#     function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
#     function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
#     #click on create roles
#     function.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
#
#     #@pytest.mark.skip(reason="This Functionality is not yet implemented(role getting create without entering name")
#     def Test_Create_Role_Without_Name(self):
#         """Function is not implemented """
#         function.driver.find_element(By.XPATH, "//a[normalize-space()='Create New Role']").click()
#
#
#         #logout
#         function.driver.find_element(By.XPATH, "//img[@alt='Header Avatar']").click()
#         function.driver.find_element(By.XPATH, "//a[@href='/logout']").click()


