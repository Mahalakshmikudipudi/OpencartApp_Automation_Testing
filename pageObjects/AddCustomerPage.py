import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath="//nav[@id='column-left']/ul/li[6]"
    lnkCustomers_menuitem_xpath="//nav[@id='column-left']/ul/li[6]/ul/li[1]"
    btn_AddNew_xpath="//i[@class='fa fa-plus']"
    txt_firstname_xpath="//input[@id='input-firstname']"
    txt_lastname_xpath="//input[@id='input-lastname']"
    txt_email_xpath="//input[@id='input-email']"
    txt_Telephone_xpath="//input[@id='input-telephone']"
    txt_Password_xpath="//input[@id='input-password']"
    txt_ConfirmPassword_xpath="//input[@id='input-confirm']"
    drp_Newsletter_xpath="//select[@id='input-newsletter']"
    drp_Status_xpath="//select[@id='input-status']"
    drp_safe_xpath="//select[@id='input-safe']"
    btn_save_xpath="//i[@class='fa fa-save']"
    success_msg_xpath="//div[@class='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver=driver

    def clickOnCustomers(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnMenuCustomers(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastName)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element(By.XPATH, self.txt_Telephone_xpath).send_keys(telephone)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)

    def setConfirmPassword(self, cpassword):
        self.driver.find_element(By.XPATH, self.txt_ConfirmPassword_xpath).send_keys(cpassword)

    def selectNewsletter(self, country):
        dropdown=Select(self.driver.find_element(By.XPATH, self.drp_Newsletter_xpath))
        dropdown.select_by_visible_text(country)

    def selectStatus(self, status):
        dropdown=Select(self.driver.find_element(By.XPATH, self.drp_Status_xpath))
        dropdown.select_by_visible_text(status)

    def selectSafe(self, safe):
        dropdown=Select(self.driver.find_element(By.XPATH, self.drp_safe_xpath))
        dropdown.select_by_visible_text(safe)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def getSuccessMessage(self):
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, self.success_msg_xpath)
            )
        ).text
        print("Message captured:", repr(msg))
        return msg











