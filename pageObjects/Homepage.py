from selenium.webdriver.common.by import By


class HomePage():
    dropdown_icon_xpath = "//i[@class='icon-down-open dropdownTriger']"
    link_Signup_linktext = "Sign In / Register"
    btn_signup_xpath = "//a[@type='button']"

    def __init__(self, driver):
        self.driver = driver

    def clickicon(self):
        self.driver.find_element(By.XPATH, self.dropdown_icon_xpath).click()

    def clickSignupRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Signup_linktext).click()

    def clickNewUserRegister(self):
        self.driver.find_element(By.XPATH, self.btn_signup_xpath).click()
