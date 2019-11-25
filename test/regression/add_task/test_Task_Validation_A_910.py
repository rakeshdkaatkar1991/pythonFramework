from lib.ui.task_page import TaskPage
from lib.utils import create_driver
from lib.ui.login_page import LoginPage
from lib.ui.home_page import HomePage
import json
import unittest
import time

class task_Validation_A_910(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_obj=LoginPage(self.driver)
        self.home_obj=HomePage(self.driver)
        self.task_obj=TaskPage(self.driver)

    #----------------Fetch Login credentials from json file----------
        data=json.load(open('./test/regression/login/A3_1234.json'))

     #----------------Login Script-------------------------------------
        self.login_obj.wait_for_login_page_load()
        self.login_obj.get_username_txtbox().send_keys(data['TC1234']['username'])
        self.login_obj.get_password_txtbox().send_keys(data['TC1234']['password'])
        self.login_obj.get_login_btn().click()

    def tearDown(self):
        #-----------Logout script------------------------------------
        self.home_obj.get_logout_btn().click()
        self.driver.close()

     #----------------Test method to add Task----------------------------------
    def test_add_Task_TC001(self):
        #------------------Fetch testdata required for add task script from json----------------------
        data=json.load(open('./test/regression/add_task/A_910.json'))
        #---------click on task tab-----------------------
        self.task_obj.get_Tasks_tab().click()
        #----------Click on add new button---------------
        self.task_obj.get_AddNew_button().click()
        time.sleep(5)
        #-----------click on New Customer Option------------
        self.task_obj.get_New_Customer_option().click()
        #----------wait for Create New Customer Page to load---------------
        time.sleep(10)
        #self.task_obj.wait_for_Create_New_Customer_Page_load()
        #-------enter value to Customer name txt box-------------------
        self.task_obj.get_Customer_Name_txtbox().send_keys(data["TC001"]["CustomerName"])
        #------------enter value to customer description field-----------
        self.task_obj.get_Customer_Description_txtbox().send_keys(data["TC001"]["CustomerDescription"])
        #---------------Click on Select customer dropdown------------------
        self.task_obj.get_Customer_drpdown().click()
        #--------------Get Customer drop down list and save it to some variable---------------------
        Cust_list=self.task_obj.get_Cust_dropdown_list()
        #-----------Get the required value from json file
        required_value=data["TC001"]["CustNamefromDrpDown"]
        #------------Loop through the list and click on required value
        size=len(Cust_list)
        for i in range(0,size):
            drpdownValue=Cust_list[i]
            text=drpdownValue.text
            if text==required_value:
                Cust_list[i].click()
                break
        else:
            print('Required value not found in dropdown')

        #--------------Click on Create Customer button--------------------
        self.task_obj.get_Create_Customer_btn()




