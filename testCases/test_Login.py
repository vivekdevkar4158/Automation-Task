import time

import pytest
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.redProperties import ReadConfig
from utilities.customLogger import LogGen
import os

@pytest.mark.usefixtures("setup")
class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
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
        time.sleep(2)
        self.lp.setEmail(self.user)
        time.sleep(2)
        self.lp.clickSubmit()
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickSubmitAfterPwd()
        time.sleep(6)

        self.targetpage = self.lp.isHomepageOpens()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")
