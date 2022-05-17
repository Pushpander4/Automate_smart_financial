from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
global driver
driver = webdriver.Chrome(ChromeDriverManager().install())
parent_handel = driver.current_window_handle

def open_browser():
    driver.maximize_window()
    driver.get("https://singular-swan-4802c7.netlify.app/")
    time.sleep(3)