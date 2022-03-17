

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

global driver

driver = webdriver.Chrome(ChromeDriverManager().install())
parent_handel = driver.current_window_handle

def open_browser():
    driver.get("https://xenodochial-stonebraker-d239bd.netlify.app/login")
    driver.maximize_window()


def login():
#    driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").clear()

#   driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("sheerin@example.com")
#    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")

#   driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("12345678")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()


