import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest

function.open_browser()
function.driver.implicitly_wait(5)
#creating login function
@pytest.fixture(scope="class")
def tc_setup():
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("def@gmail.com")
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Def123456@")
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    # test teardown takes place after yield
    yield

@pytest.fixture(scope="class")
def get_data():
    return ["def@gmail.com", "Def123456@", "Def123456@"]
