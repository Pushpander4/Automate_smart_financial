import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  time

global driver

driver = webdriver.Chrome(ChromeDriverManager().install())
parent_handel = driver.current_window_handle

def open_browser():
    driver.maximize_window()
    driver.get("https://xenodochial-stonebraker-d239bd.netlify.app/login")
    print("Title Name", driver.title)

def login():
    driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").clear()
    time.sleep(5)
 #   driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("sheerin@example.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").clear()
    time.sleep(5)
 #   driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("12345678")
 #   driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").double_click
    time.sleep(15)
