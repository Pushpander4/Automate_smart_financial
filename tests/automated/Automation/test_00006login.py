import time
import pytest
from Automation import funtion
from selenium.webdriver.common.by import By

funtion.open_browser()
@pytest.mark.usefixtures("get_Data")
class Test_Login():
    def test_smart_financial_title_image(self):
        funtion.driver.find_element(By.CSS_SELECTOR,".text-center.p-4").is_enabled()


    def test_email_input_field(self):
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").is_enabled()


    def test_password_input_field(self):
        funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").is_enabled()

    def test_email_text(self):
        text_email = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Email']").text
        assert (text_email == "Email"), 'TEST-LOGIN-1 "Email" text should be present'


    def test_password_text(self):
        text_password = funtion.driver.find_element(By.XPATH,"//label[normalize-space()='Password']").text
        assert (text_password == "Password") , 'TEST-LOGIN-1 "Passsword" text should be present'


    def test_remember_me_text(self):
        text_on_remember = funtion.driver.find_element(By.XPATH,"//label[@for='customControlInline']").text
        assert (text_on_remember == "Remember me")


    def test_text_2022_smart_financial(self):
        t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 SmartFinancial']").text
        assert (t_2022_Smart_Financial == "© 2022 SmartFinancial")


    def test_remember_me(self):
        funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_enabled()
        funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").click()
        v1 = funtion.driver.find_element(By.XPATH, "//input[@id='customControlInline']").is_selected()
        assert (v1 == True)
        time.sleep(4)

    def test_login(self, get_Data):
        funtion.driver.refresh()
        funtion.driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys(get_Data[0])
        funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(get_Data[2])
        time.sleep(5)


    def test_login_button_text(self):
        text_on_login_button = funtion.driver.find_element(By.XPATH,"//button[@type='submit']").text
        assert (text_on_login_button == "Log In")


    def test_login_button(self):
        funtion.driver.find_element(By.XPATH, "//button[@type='submit']").click()


    @pytest.mark.skip
    def test_able_to_login(self):
        time.sleep(2)
        profile_page_url= (funtion.driver.current_url)
        assert (profile_page_url == "https://xenodochial-stonebraker-d239bd.netlify.app/profile")