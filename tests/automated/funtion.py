

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



# driver = webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# parent_handel = driver.current_window_handle

def open_browser():
    global driver
    driver.maximize_window()
    driver.get("https://xenodochial-stonebraker-d239bd.netlify.app/login")
    time.sleep(3)










