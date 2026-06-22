import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    print(logger)

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("***************** Test_003_AddCustomer ******************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickAlert()
        self.logger.info("*************Login Successful ***********************")

        self.logger.info("*************** Starting Add Customer Test ********************")

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomers()
        self.addCust.clickOnMenuCustomers()
        self.addCust.clickOnAddNewCustomer()

        self.logger.info("************** Providing customer info **********************")
        self.addCust.setFirstName("Shaanvi")
        self.addCust.setLastName("Kudipudi")
        email = random_email_generator()
        self.addCust.setEmail(email)
        self.addCust.setTelephone("8995655224")
        self.addCust.setPassword("shaanvi@20")
        self.addCust.setConfirmPassword("shaanvi@20")
        self.addCust.selectNewsletter("Disabled")
        self.addCust.selectStatus("Enabled")
        self.addCust.selectSafe("Yes")
        self.addCust.clickOnSave()

        self.logger.info("**************** Saving the customer info ***************")

        self.logger.info("************** Add customer validation started *****************")

        msg = self.addCust.getSuccessMessage()

        if 'Success: You have modified customers!' in msg:
            assert True
            self.logger.info("************** Add Customer Test Passed *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") #Screenshot
            self.logger.error("**************** Add Customer Test Failed *********************")
            assert False

        self.driver.close()

def random_email_generator():
    chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return chars + "@gmail.com"


