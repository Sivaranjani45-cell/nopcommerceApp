import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txt_Email_xpath="//input[@id='SearchEmail']"
    txt_Password_xpath="//input[@id='Password']"
    txt_firstName_xpath="//input[@id='SearchFirstName']"
    txt_lastName_xpath="//input[@id='SearchLastName']"
    rdMaleGenderId="//input[@id='Gender_Male']"
    rfFemaleGenderId="//input[@id='Gender_Female']"
    txt_Companyname_xpath="//input[@id='Company']"
    txtcustomerRoles_xpath="//span[@aria-expanded='true']//input[@role='searchbox']"
    listitemsAdministrator_xpath="//li[@title='Administrators']"
    listitemsRegistered_xpath="//li[@title='Registered']"
    listitems_Guests_xpath="//li[@title='Guests']"
    listitems_vendors_xpath="//li[@title='Vendors']"
    listiems_moderators_xpath="//li[@title='Forum Moderators']"
    drpdownVendor_xpath="//select[@id='VendorId']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def __init__(self,driver):
       self.driver=driver

    def clickoncustomermenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()
    def clickoncustomermenuitem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()
    def clickonaddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()
    def setemail(self,email):
        self.driver.find_element_by_xpath(self.txt_Email_xpath).send_keys(email)
    def setpassword(self,password):
        self.driver.find_element_by_xpath(self.txt_Password_xpath).send_keys(password)

    def setcustomerroles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role =='Registered':
           self.listitem=self.driver.find_element_by_xpath(self.listitemsRegistered_xpath)
        elif role=='Administrators':
           self.listitem=self.driver.find_element_by_xpath(self.listitemsAdministrator_xpath)
        elif role=='Guests':
           time.sleep(3)
           self.driver.find_element_by_xpath("//input[@class='select2-search__field valid']").click()
           self.listitem = self.driver.find_element_by_xpath(self.listitems_Guests_xpath)
        elif role=='Vendors':
           self.listitem = self.driver.find_element_by_xpath(self.listitems_vendors_xpath)
        else:
           self.listitem = self.driver.find_element_by_xpath(self.listitems_Guests_xpath)

    def setmanagerofvendor(self,value):
         drp=Select(self.driver.find_element_by_xpath(self.drpdownVendor_xpath))
         drp.select_by_visible_text(value)
    def setgender(self,gender):
         if gender=='male':
           self.driver.find_element_by_id(self.rdMaleGenderId).click()
         elif gender=='female':
           self.driver.find_element_by_id(self.rfFemaleGenderId).click()
         else:
           self.driver.find_element_by_id(self.rdMaleGenderId).click()
    def setfirstname(self,fname):
        self.driver.find_element_by_xpath(self.txt_firstName_xpath).send_keys(fname)
    def setlastname(self,lname):
        self.driver.find_element_by_xpath(self.txt_lastName_xpath).send_keys(lname)
    def setcompanyname(self,comname):
        self.driver.find_element_by_xpath(self.txt_Companyname_xpath).send_keys(comname)
    def setadmincontent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)
    def clickonsave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
