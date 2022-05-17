import time
from Automation import function
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pytest


function.open_browser()
# User management fields test
@pytest.mark.usefixtures('tc_setup')
class TestCampaignsMainPage:
    def test_campaigns_on_side_bar(self):
        text_campaigns_drop = function.driver.find_element(By.XPATH, "//span[normalize-space()='Campaigns']").text
        assert text_campaigns_drop == "Campaigns", "Value of text is not 'Campaigns'"
        time.sleep(4)

    def test_enabled_campaigns_button(self):
        function.driver.find_element(By.XPATH, "//span[normalize-space()='Campaigns']").is_enabled()
        function.driver.find_element(By.XPATH, "//span[normalize-space()='Campaigns']").click()
    def test_status_lable(self):
        text_campaigns_drop = function.driver.find_element(By.XPATH, "//label[normalize-space()='Status']").text
        assert text_campaigns_drop == "Status", "Value of text is not 'Status'"

    def test_product_lable(self):
        text_product_drop = function.driver.find_element(By.XPATH, "//label[normalize-space()='Product']").text
        assert text_product_drop == "Product", "Value of text is not 'Status'"

    def test_type_lable(self):
        text_type_drop = function.driver.find_element(By.XPATH, "//label[normalize-space()='Type']").text
        assert text_type_drop == "Type", "Value of text is not 'type'"

    #TODO:- "Need to write scripts for dropdown"
    def test_text_on_create_new_campagin_button(self):
        text_type_drop = function.driver.find_element(By.XPATH, "//a[@class='btn btn-sfpink']").text
        assert text_type_drop == "New Campaign", "Value of text is not 'New Campaign'"

    def test_enable_of_create_new_campagin_button(self):
        function.driver.find_element(By.XPATH, "//a[@class='btn btn-sfpink']").is_enabled()

    def test_create_new_campagin(self):
        function.driver.find_element(By.XPATH, "//a[@class='btn btn-sfpink']").click()




