import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest

function.open_browser()
function.driver.implicitly_wait(5)
time.sleep(5)

@pytest.mark.usefixtures("tc_setup")
class Test_role_delection():
    def test_delete_role(self):
        function.driver.find_element(By.XPATH, "//a[@class='has-arrow']").click()
        function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        #function.driver.find_element(By.XPATH, "//a[normalize-space()='Roles']").click()
        time.sleep(4)

    def test_abc(self):
        card_elements = function.driver.find_elements(By.CLASS_NAME, "card")

        for card_elem in card_elements:
            title_elem = card_elem.find_element(By.XPATH, "//a[@class='text-dark']")
            if title_elem.text == "aac":
                card_elem.find_element(By.XPATH, "//i[@class='bx bx-trash text-muted']").click()
                break
        time.sleep(2)

        function.driver.find_element(By.XPATH, "//button[normalize-space()='Confirm & Delete']").click()





