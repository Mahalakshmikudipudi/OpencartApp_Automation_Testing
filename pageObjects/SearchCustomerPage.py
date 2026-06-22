import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomer:
    #Add customer page
    txtCustName_id="input-name"
    txtEmail_id="input-email"
    btnFilter_id="button-filter"

    tblSearchResults_xpath="//table[@class='table table-bordered table-hover']"
    tblRows_xpath="//table[@class='table table-bordered table-hover']//tbody/tr"
    tableColumns_xpath="//table[@class='table table-bordered table-hover']//tbody/tr/td"

    def __init__(self, driver):
        self.driver=driver

    def setCustomerName(self, customerName):
        self.driver.find_element(By.ID, self.txtCustName_id).clear()
        self.driver.find_element(By.ID, self.txtCustName_id).send_keys(customerName)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def clickOnFilter(self):
        self.driver.find_element(By.ID, self.btnFilter_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.tblSearchResults_xpath)
            emailid=table.find_element(By.XPATH, "//table[@class='table table-bordered table-hover']//tbody/tr["+str(r)+"]/td[3]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.tblSearchResults_xpath)
            Name=table.find_element(By.XPATH, "//table[@class='table table-bordered table-hover']//tbody/tr["+str(r)+"]/td[2]").text
            if Name == name:
                flag = True
                break
        return flag

