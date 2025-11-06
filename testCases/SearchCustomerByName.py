import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestSearchCustomerbyname:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
@pytest.mark.regression
def test_searchcustomerbyname(self,setup):
    self.logger.info("Search Customer By Name")
    self.driver=setup
    self.driver.get(self.baseURL)
    self.driver.maximize_window()
    self.lp=LoginPage()
    self.lp.setusername(self.username)
    self.lp.setpassword(self.password)
    self.lp.clicklogin()
    self.logger.info("Login successful")
    self.logger.info("Starting Search Customer by name")
    self.addcust=AddCustomer(self.driver)
    self.addcust.clickoncustomermenu()
    self.addcust.clickoncustomermenuitem()
    self.logger.info("Searching Customer by name")
    searchcust=SearchCustomer(self.driver)
    searchcust.setfirstname("Pratik")
    searchcust.setlastname("Patil")
    searchcust.clicksearch()
    time.sleep(3)
    status=searchcust.searchcustomerbyname("Pratik Patil")
    assert True==status
    self.logger.info("TcSearchCustomerByEmail finished")
    self.driver.close()

