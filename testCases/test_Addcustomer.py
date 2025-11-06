import pytest
# import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class TestAddCustomer:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("***TestAddCustomer***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login successful**")
        self.logger.info("**Starting Add Customer Testcase")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomermenuitem()
        self.addcust.clickonaddnew()
        self.logger.info("**Providing Customer info**")
        self.email= self.random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword(self.password)
        self.addcust.setcustomerroles("Guests")
        self.addcust.setmanagerofvendor("Vendor2")
        self.addcust.setgender("Male")
        self.addcust.setfirstname("Siva")
        self.addcust.setlastname("Ranjani")
        self.addcust.setcompanyname("Qway Tech")
        self.addcust.setadmincontent("This is for testing")
        self.addcust.clickonsave()
        self.logger.info("**Saving Customer info**")
        self.logger.info("**Customer validation started**")

        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)


        if "Customer has been added successfully" in self.msg:
            assert True==True
            self.logger.info("Add Customer test Case passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test Customer_scr.png")
            self.logger.error("Add Customer test case failed ")
            assert True==False
        self.driver.close()
        self.logger.info("Ending Add Customer Test")






