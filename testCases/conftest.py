import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.......................")
        #driver.maximize_window()
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.......................")
        #driver.maximize_window()
    return driver


def pytest_addoption(parser): #this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")


########################### PyTest HTML Report ################################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Opencart"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Mahalakshmi"

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)