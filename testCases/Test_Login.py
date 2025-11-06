
import pytest
import time
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class TestLogin:
    baseURL=ReadConfig.getapplicationurl()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("********TestLogin******")
        self.logger.info("*****Verifying Home Page Title******")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        time.sleep(5)
        self.driver.close()
        if act_title =="nopCommerce demo store.Login":
           assert True
           self.driver.close()
           self.logger.info("*******Home Page title is passed******")
        else:
           self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
           self.driver.close()
           self.logger.info("*******Home Page Title is failed****")
           assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*****Verifying Login test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        time.sleep(5)
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
          assert True
          self.logger.info("****Login test is passed***")
          self.driver.close()
        else:
          self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
          self.driver.close()
          self.logger.error("****Login test is failed****")
          assert False



