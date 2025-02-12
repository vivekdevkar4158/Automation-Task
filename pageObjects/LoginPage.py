from selenium.webdriver.common.by import By


class LoginPage():
    checkbox_LoginWithEmail_ID = "logtypeboxemail"
    txt_email_Xpath = "//form[@id='fchknum_form']//input[@id='mobilenumber']"
    btn_submit_ID = "fchknum"
    txt_password_Xpath = "//input[@id='login_password']"
    btn_submitAfterPwd_Xpath = "//button[@id='fwithotp']"
    element_homepage = "//li[@class='noDisplayMb']"  # "Online Shopping for Premium Mens Clothes and Accessories | Zodiac"

    def __init__(self, driver):
        self.driver = driver

    def setCheckbox(self):
        self.driver.find_element(By.ID, self.checkbox_LoginWithEmail_ID).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_Xpath).send_keys(email)

    def clickSubmit(self):
        self.driver.find_element(By.ID, self.btn_submit_ID).click()

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_Xpath).send_keys(pwd)

    def clickSubmitAfterPwd(self):
        self.driver.find_element(By.XPATH, self.btn_submitAfterPwd_Xpath).click()

    def isHomepageOpens(self):
        try:
            return self.driver.find_element(By.XPATH, self.element_homepage).is_displayed()
        except:
            return False
