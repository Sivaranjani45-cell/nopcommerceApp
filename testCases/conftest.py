from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    # driver=webdriver.Edge()
    # return driver
    if browser=='chrome':
      driver=webdriver.Chrome()
    elif browser=='firefox':
      driver=webdriver.Firefox()
    else:
      driver=webdriver.Ie()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser (request):
    return request.config.getoption("--browser")
#####Pytest HTML Reports#######
# def pytest_configure(config):
#     config.metadata['Project Name']='nop Commerce'
#     config.metadata['Module Name']='Customer'
#     config.metadata['Tester']='Siva'
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME",None)
#     metadata.pop("Plugins",None)