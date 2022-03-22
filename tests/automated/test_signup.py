from automated import funtion
from selenium.webdriver.common.by import By


funtion.open_browser()

def test_signup():
    text_on_signup = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").text
    assert (text_on_signup == "Signup now")

def testClick_signup():
        funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Signup now']").click()

def testFree_Register():
    Free_Register_text=funtion.driver.find_element(By.XPATH ,"//h5[normalize-space()='Free Register']").text
    assert ( Free_Register_text == "Free Register")

def test_Get_your_free_Smart_Financial_account_now():
    text_Get_your_free_Smart_Financial_account_now = funtion.driver.find_element(By.XPATH ,"//p[normalize-space()='Get your free Smart Financial account now.']").text
    assert (text_Get_your_free_Smart_Financial_account_now == "Get your free Smart Financial account now.")



def testEnter_full_name():
    Enter_full_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Name']").text
    assert (Enter_full_name == "Name")
    # text_name = funtion.driver.find_element(By.XPATH, "//div[normalize-space()='Please Enter Your Username']").text
    # print(text_name)

def testEnter_full_name_holder():
    Enter_full_name_holder = funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Full Name']").get_attribute("placeholder")
    assert (Enter_full_name_holder == "Enter Full Name")



def testEnter_company_name_holder():
    Enter_company_name_holder = funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Company Name']").get_attribute("placeholder")
    assert (Enter_company_name_holder == "Enter Company Name")

def testEnter_company_name():
    Enter_company_name = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Company Name']").text
    assert (Enter_company_name == "Company Name")



def testEnter_email_place_holder():
    Enter_email_place_holder = funtion.driver.find_element(By.XPATH, "//input[@id='email']").get_attribute("placeholder")
    assert (Enter_email_place_holder == "Enter email")


def testEnter_email_place():
    Enter_email_place = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Email']").text
    assert (Enter_email_place == "Email")



def testplace_holder_Enter_Password():
    place_holder_Enter_Password = funtion.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").get_attribute("placeholder")
    assert (place_holder_Enter_Password == "Enter Password")

def testEnter_Password():
    Enter_Password = funtion.driver.find_element(By.XPATH, "//label[normalize-space()='Password']").text
    assert (Enter_Password == "Password")

def test_text_on_button_register():
    text_on_button_register = funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").text
    assert (text_on_button_register == "Register")

def test_click_button_register():
    funtion.driver.find_element(By.XPATH, "//button[normalize-space()='Register']").click()



def test_text_by_registering_you_agree_to_the():
    text_by_registering_you_agree_to_the = funtion.driver.find_element(By.XPATH, "//p[@class='mb-0']").text

    assert (text_by_registering_you_agree_to_the == "By registering you agree to the Terms of Use")

def test_text_click_terms_of_use():
    text_click_terms_of_use = funtion.driver.find_element(By.XPATH,"//a[normalize-space()='Terms of Use']").text
    assert (text_click_terms_of_use == "Terms of Use")

def test_click_terms_of_use():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Terms of Use']").click()

def test_already_have_an_account():
    t_already_have_an_account = funtion.driver.find_element(By.XPATH,"//div[@class='mt-5 text-center']//p").text
    print(t_already_have_an_account)
    assert (t_already_have_an_account == "Already have an account ? Login")

def testbacktologin():
    text_on_login_back = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
    assert (text_on_login_back == "Login")

def test_click_on_login_button_to_go_back_to_login_page():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

def testtext_2022_Smart_Financial():
    t_2022_Smart_Financial = funtion.driver.find_element(By.XPATH,"//p[normalize-space()='© 2022 Smart Financial']").text
    assert (t_2022_Smart_Financial == "© 2022 Smart Financial")









def testbacktologin():
    text_on_login_back = funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").text
    assert (text_on_login_back == "Login")

def test_click_on_login_button_to_go_back_to_login_page():
    funtion.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()


