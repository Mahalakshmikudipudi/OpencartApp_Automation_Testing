import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    print(logger)

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************* Test_001_Login **********************")
        self.logger.info("********************* Verifying Home Page Title **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Administration":
            assert True
            self.logger.info("******************* Home page title test is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("******************* Home page title test is failed *********************")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************* Verifying the login test *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickAlert()
        time.sleep(5)
        act_title=self.driver.title
        if act_title=="Dashboard":
            assert True
            self.logger.info("******************* Login test is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("******************* Login test is failed *********************")
            assert False
        self.driver.close()
