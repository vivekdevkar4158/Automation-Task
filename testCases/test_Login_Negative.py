

import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.redProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_Login_Negative():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    invalid_user = "invalid_user@example.com"  # Example invalid email
    invalid_password = "wrong_password"        # Example invalid password

    def test_invalid_login(self, setup):
        self.logger.info("******* Starting test_invalid_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("** Launching Application **")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("** Clicking on icon **")
        self.hp.clickicon()
        time.sleep(3)
        self.logger.info("** Clicking on SignupRegister **")
        self.hp.clickSignupRegister()

        self.lp = LoginPage(self.driver)
        self.lp.setCheckbox()
        time.sleep(3)
        self.logger.info("** Entering invalid email **")
        self.lp.setEmail(self.invalid_user)  # Invalid email
        time.sleep(3)
        self.lp.clickSubmit()
        time.sleep(6)

        # Verify URL ends with the entered email
        current_url = self.driver.current_url
        expected_url_suffix = f"?email={self.invalid_user}"

        if current_url.endswith(expected_url_suffix):
            self.logger.info("** Test Passed: Redirected to expected page with email in URL **")
            assert True
        else:
            self.logger.error(f"** Test Failed: URL did not match expected. Actual URL: {current_url} **")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_invalid_login.png")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_invalid_login **********")

        # try:
        #     # Wait for the "Create an Account" button to be visible
        #     create_account_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//button[@title='Create an Account']"))
        #     )
        #     is_register_page = create_account_button.is_displayed()
        # except Exception as e:
        #     self.logger.error(f"** Test Failed: 'Create an Account' button not found. Error: {str(e)} **")
        #     is_register_page = False
        #
        #     # Assert if the test should pass or fail
        # assert is_register_page, "** Test Failed: 'Create an Account' button not found on registration page **"
        #
        # if is_register_page:
        #     self.logger.info("** Test Passed: Successfully redirected to the registration page **")
        # else:
        #     # Capture a screenshot in case of failure
        #     screenshot_path = os.path.abspath(os.curdir) + "\\screenshots\\" + "test_invalid_login.png"
        #     self.driver.save_screenshot(screenshot_path)
        #     self.logger.info(f"** Screenshot saved at: {screenshot_path} **")
        #
        # self.driver.close()
        # self.logger.info("******* End of test_invalid_login **********")

        # try:
        #     # Wait for registration page element to be visible
        #     register_page_element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Register']"))
        #     )
        #     is_register_page = register_page_element.is_displayed()
        # except Exception as e:
        #     self.logger.error(f"** Test Failed: Registration page not found. Error: {str(e)} **")
        #     is_register_page = False
        #
        #     # Assert if the test should pass or fail
        # assert is_register_page, "** Test Failed: Invalid email did not redirect to the registration page **"
        #
        # if is_register_page:
        #     self.logger.info("** Test Passed: Invalid email redirected to registration page **")
        # else:
        #     # Capture a screenshot in case of failure
        #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_invalid_login.png")
        #
        # self.driver.close()
        # self.logger.info("******* End of test_invalid_login **********")
