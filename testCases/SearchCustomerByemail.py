import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestSearchCustomerbyemail:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
@pytest.mark.regression
def test_searchcustomerbyemail(self,setup):
    self.logger.info("Search Customer By Email")
    self.driver=setup
    self.driver.get(self.baseURL)
    self.driver.maximize_window()
    self.lp=LoginPage()
    self.lp.setusername(self.username)
    self.lp.setpassword(self.password)
    self.lp.clicklogin()
    self.logger.info("Login successful")
    self.logger.info("Starting Search Customer by email")
    self.addcust=AddCustomer(self.driver)
    self.addcust.clickoncustomermenu()
    self.addcust.clickoncustomermenuitem()
    self.logger.info("Searching Customer by email")
    searchcust=SearchCustomer(self.driver)
    searchcust.setemail("pratikpatil123456@gmail.com")
    searchcust.clicksearch()
    time.sleep(3)
    status=searchcust.searchcustomerbyemail("pratikpatil123456@gmail.com")
    assert True==status
    self.logger.info("TcSearchCustomerByEmail finished")
    self.driver.close()



