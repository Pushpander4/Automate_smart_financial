import time
from Automation import funtion
from selenium.webdriver.common.by import By
import pytest

funtion.open_browser()
funtion.driver.implicitly_wait(5)
#creating login function
@pytest.fixture(scope="class")
def tc_setup():
    profile_page_url = funtion.driver.current_url
    print('piyush tc_setup ' + profile_page_url)
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("piyush@ikshalabs.com")
    funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@009")
    funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    yield
    # funtion.driver.find_element(By.XPATH,"//button[@id='page-header-user-dropdown']").click()
    # funtion.driver.find_element(By.XPATH,"//span[normalize-space()='Logout']").click()


@pytest.fixture(scope="class")
def get_Data():
    return ["piyush@ikshalabs.com", "Piyush@123", "Piyush@009"]
