from lib.ui.login_page import LoginPage
from lib.ui.add_user_page import AddUser
from lib.utils import create_driver
from selenium.webdriver import ActionChains
import json
import unittest
import time

class addUser_A5678(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_page_obj=LoginPage(self.driver)
        self.addUser_page_obj=AddUser(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_addUser_TC001(self):
        data=json.load(open('./test/regression/add_user/A3_5678.json'))
        self.login_page_obj.wait_for_login_page_load()
        #----------------------Login script--------------------
        #enter login credentials
        self.login_page_obj.get_username_txtbox().send_keys(data["TC5678"]["LoginUserName"])
        self.login_page_obj.get_password_txtbox().send_keys(data["TC5678"]["LoginPassword"])
        self.login_page_obj.get_login_btn().click()

        #----------------------Add User script--------------------
        #click on New Users tab
        self.addUser_page_obj.get_User_tab().click()
        #Click on New User button
        self.addUser_page_obj.get_New_User_button().click()
        #Enter first name
        time.sleep(5)
        self.addUser_page_obj.get_First_Name_txtbox().send_keys(data["TC5678"]["FirstName"])
        #Enter last name
        self.addUser_page_obj.get_Last_Name_txtbox().send_keys(data["TC5678"]["LastName"])
        #Enter email id
        self.addUser_page_obj.get_Email_Id_txtbox().send_keys(data["TC5678"]["Email_ID"])
        #Enter UserName
        self.addUser_page_obj.get_UserName_txtbox().send_keys(data["TC5678"]["UserName"])
        #Enter Password
        self.addUser_page_obj.get_Password_txtbox().send_keys(data["TC5678"]["Password"])
        #Enter RetypePassword
        self.addUser_page_obj.get_ReType_Password_txtbox().send_keys(data["TC5678"]["RetypePassword"])

        #Select value from department dropdown using ActionChains functionality
        time.sleep(5)
        dept=self.addUser_page_obj.get_Department_dropdown()
        act=ActionChains(self.driver)
        time.sleep(5)
        act.move_to_element(dept).click().perform()
        act.move_to_element(data["TC5678"]["DeptDropdownValue"])
        #Click on Create button
        time.sleep(5)
        self.addUser_page_obj.get_Create_button().click()





