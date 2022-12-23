from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="E:\\chrome driver\\chromedriver_win32\\chromedriver.exe")
    return driver

# Run testcases on desired browser------------------
# @pytest.fixture()
# def setup(browser):
#     if browser=='chrome':
#         driver=webdriver.Chrome(executable_path="E:\\chrome driver\\chromedriver_win32\\chromedriver.exe")
#         return driver
#         print("Launching chrome browser.........")
#     elif browser=='firefox':
#         driver = webdriver.Firefox()
#         return driver
#         print("Launching firefox browser.........")
#     else:
#         driver = driver=webdriver.Chrome(executable_path="E:\\chrome driver\\chromedriver_win32\\chromedriver.exe")
#         return driver
#
# def pytest_addoption(parser):    # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")

# PyTEst HTML Report

def pytest_configure (config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Pankaj'

# It is hook for delete/modify Environment info to HTML Reports

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)

