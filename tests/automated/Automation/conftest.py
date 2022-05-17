import random
import time
from Automation import function
from selenium.webdriver.common.by import By
import pytest
import faker
from pydictobject import DictObject

function.open_browser()
function.driver.implicitly_wait(5)
fake = faker.Faker()  #global variable
#creating login function


@pytest.fixture(scope="class")
def tc_setup():
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("piyush.wadhwa.703@gmail.com")
    function.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Piyush@009")
    function.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    # test teardown takes place after yield
    yield

@pytest.fixture(scope="class")
def get_data():
    return DictObject({
        "email": fake.unique.email(),
        "invalid_password": "Piyush123",
        "self_email": "piyush.wadhwa.703@gmail.com",
        "self_password": "Piyush@009",
        "role_name": "Team member" + str(random.randint(100000, 999999)),
        "first_name": fake.unique.first_name(),
        "last_name": fake.unique.last_name(),
    })