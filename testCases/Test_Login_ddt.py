
import pytest
import time
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
class TestDDTLogin:
    baseURL=ReadConfig.getapplicationurl()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    def __init__(self):
        self.driver = None

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*******TestDDTLogin******")
        self.logger.info("*****Verifying Login DDT*****")
        self.driver.get(self.baseURL)
        self.lp=LoginPage()
        self.rows=ExcelUtils.getrowcount(self.path,'Sheet1')
        print("No.of rows in a excel:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readdata(self.path,'Sheet1',r,1)
            self.password=ExcelUtils.readdata(self.path,'Sheet1',r,2)
            self.exp=ExcelUtils.readdata(self.path,'Sheet1',r,3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("Passed")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Failed")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp =="Pass":
                    self.logger.info("Failed")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***Passed")
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("Login DDT Test passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT Test failed")
                self.driver.close()
                assert False
        self.logger.info("End of Login DDT")
        self.logger.info("Completed test_login_ddt")






