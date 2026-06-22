import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    logger=LogGen.loggen()
    print(logger)

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************* Test_002_DDT_Login ***************************")
        self.logger.info("******************* Verifying the login test *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel", self.rows)

        lst_status=[] # Empty list variable
        for r in range(2, self.rows+1):
            self.Username=XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Password=XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.Username)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard - End Point Ecommerce - Admin Portal"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("******************* Login test is passed *********************")
                    self.lp.clickLogout()
                    lst_status.append("Passed")
                elif self.exp=="Fail":
                    self.logger.info("******************* Login test is Failed *********************")
                    self.lp.clickLogout()
                    lst_status.append("Failed")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("******************* Login test is failed *********************")
                    lst_status.append("Failed")
                elif self.exp=="Fail":
                    self.logger.info("******************* Login test is Passed *********************")
                    lst_status.append("Passed")
        if "Failed" not in lst_status:
            self.logger.info("****************** Login DDT test passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****************Login DDT test failed ******************")
            self.driver.close()
            assert False
        self.logger.info("************** End of Login DDT Test ********************")
        self.logger.info("*************** Completed TC_Login_DDT_002 ********************")