import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest

function.open_browser()
function.driver.implicitly_wait(5)
#creating login function
@pytest.fixture(scope="class")
def tc_setup():
    profile_page_url = function.driver.current_url
    print('piyush tc_setup ' + profile_page_url)
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("piyush@ikshalabs.com")
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@009")
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    yield
    # funtion.driver.find_element(By.XPATH,"//button[@id='page-header-user-dropdown']").click()
    # funtion.driver.find_element(By.XPATH,"//span[normalize-space()='Logout']").click()


@pytest.fixture(scope="class")
def get_Data():
    return ["piyush@ikshalabs.com", "Piyush@123", "Piyush@009"]
