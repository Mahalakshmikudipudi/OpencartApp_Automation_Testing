import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    print(logger)

    @pytest.mark.regression
    def test_SearchCustomerByName(self, setup):
        self.logger.info("***************** SearchCustomerByName_005 ******************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickAlert()
        self.logger.info("*************Login Successful ***********************")

        self.logger.info("*********** Starting Search Customer By Name *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomers()
        self.addcust.clickOnMenuCustomers()

        self.logger.info("************ Searching Customer By Name *****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setCustomerName("Koushik Kudipudi")
        searchcust.clickOnFilter()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Koushik Kudipudi")
        assert True == status
        self.logger.info("************* TC_SearchCustomerByName_004 Finished ************")
        self.driver.close()