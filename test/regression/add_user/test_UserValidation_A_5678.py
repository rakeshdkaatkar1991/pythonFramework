from lib.ui.login_page import LoginPage
from lib.ui.user_page import User
from lib.utils import create_driver
from lib.ui.home_page import HomePage
import json
import unittest
import time

class UserValidation_A5678(unittest.TestCase):

    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_page_obj=LoginPage(self.driver)
        self.user_page_obj=User(self.driver)
        self.home_page_obj=HomePage(self.driver)
        #-----------Fetch login credentials from Json file-----------------------
        data = json.load(open('./test/regression/add_user/A3_5678.json'))

        # ----------------------Login script--------------------
        # enter login credentials
        self.login_page_obj.wait_for_login_page_load()
        self.login_page_obj.get_username_txtbox().send_keys(data["TC001"]["LoginUserName"])
        self.login_page_obj.get_password_txtbox().send_keys(data["TC001"]["LoginPassword"])
        self.login_page_obj.get_login_btn().click()


    def tearDown(self):
        # -----------Logout script------------------------------------
        self.home_page_obj.get_logout_btn().click
        self.driver.close()

    #Test method to add User
    def test_validateUser_TC001(self):
        #----------------------Validate User script--------------------
        data = json.load(open('./test/regression/add_user/A3_5678.json'))
        #click on New Users tab
        self.user_page_obj.get_User_tab().click()
        #Click on New User button
        self.user_page_obj.get_New_User_button().click()
        #Enter first name
        time.sleep(5)
        self.user_page_obj.get_First_Name_txtbox().send_keys(data["TC001"]["FirstName"])
        #Enter last name
        self.user_page_obj.get_Last_Name_txtbox().send_keys(data["TC001"]["LastName"])
        #Enter email id
        self.user_page_obj.get_Email_Id_txtbox().send_keys(data["TC001"]["Email_ID"])
        #Enter UserName
        self.user_page_obj.get_UserName_txtbox().send_keys(data["TC001"]["UserName"])
        #Enter Password
        UserName=data["TC001"]["UserName"]
        self.user_page_obj.get_Password_txtbox().send_keys(data["TC001"]["Password"])
        time.sleep(2)
        #Enter RetypePassword
        self.user_page_obj.get_ReType_Password_txtbox().send_keys(data["TC001"]["RetypePassword"])
        time.sleep(2)
        #Select value from department dropdown using foreach loop
        self.user_page_obj.get_Department_dropdown().click()
        itemlist=self.user_page_obj.get_ddl_values()
        required_Value='Quality Control'
        for element in itemlist:
            text = element.text
            if text==required_Value:
                element.click()
                break
        else:
            print("Required value not present in ddl")

        #Click on ActiPlan togglebutton
        self.user_page_obj.get_Actiplans_Togglebtn().click()
        #Click on Create button
        self.user_page_obj.wait_for_create_button_to_click()
        time.sleep(5)
        self.user_page_obj.get_Create_button().click()
        time.sleep(2)

    #-------------------This section is to delete User--------------------
        time.sleep(5)
        #click on Name link
        self.user_page_obj.get_First_User_cell(UserName).click()
        #click on Delete button
        time.sleep(5)
        self.user_page_obj.get_Delete_button().click()
        time.sleep(5)
        # Switch the control to the Alert window
        alt=self.driver.switch_to.alert
        # use the accept() method to accept the alert
        time.sleep(5)
        alt.accept()
        time.sleep(5)


















