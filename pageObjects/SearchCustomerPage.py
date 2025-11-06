


class SearchCustomer:
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="SearchCustomer"

    table_xpath="//*[@id='customers-grid_wrapper']"
    tableRows_xpath="//*[@id='customers-grid_wrapper']//tbody/tr"
    tableColumns_xpath="//*[@id='customers-grid_wrapper']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver
    def setemail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)
    def setfirstname(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)
    def setlastname(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)
    def clicksearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()
    def getnoofrows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))
    def getnoofcolumns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))
    def searchcustomerbyemail(self,email):
        flag=False
        for r in range(1,self.getnoofrows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//*[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag
    def searchcustomerbyname(self,name):
        flag=False
        for r in range(1,self.getnoofrows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            Name=table.self.driver.find_element_by_xpath("//*[@id='customers-grid_wrapper']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
        return flag





