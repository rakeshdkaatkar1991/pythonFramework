from lib.ui.task_page import TaskPage
from lib.utils import create_driver
from lib.ui.login_page import LoginPage
from lib.ui.home_page import HomePage
import json
import unittest
import time
import pdb

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
        time.sleep(3)
        #---------click on task tab-----------------------
        self.task_obj.get_Tasks_tab().click()

        #Test script to add Customer------------------------------------
        #----------Click on add new button---------------
        self.task_obj.get_AddNew_button().click()
        time.sleep(5)
        #-----------click on New Customer Option------------
        #self.task_obj.get_ddl_from_AddNew('+ New Customer')
        self.task_obj.get_options_from_dropdown('+ New Customer',self.task_obj.get_Add_New_ddl(),self.task_obj.get_New_Customer_option('+ New Customer'))
        #self.task_obj.get_New_Customer_option().click()
        #----------wait for Create New Customer Page to load---------------
        time.sleep(10)
        #self.task_obj.wait_for_Create_New_Customer_Page_load()
        #-------enter value to Customer name txt box-------------------
        self.task_obj.get_Customer_Name_txtbox().send_keys(data["TC001"]["CustomerName"])
        #------------enter value to customer description field-----------
        self.task_obj.get_Customer_Description_txtbox().send_keys(data["TC001"]["CustomerDescription"])
        #---------------Click on Select customer dropdown------------------
        self.task_obj.get_Customer_drpdown().click()
        #--------------Get Customer drop down list and Split it then save it to some variable---------------------
        self.task_obj.get_options_from_dropdown('Galaxy Corporation',self.task_obj.get_Cust_dropdown_list(),self.task_obj.get_Required_Project_option('Galaxy Corporation'))
        #-------------Use scroll option of js----------------------
        js_command='window.scroll(0,5000)'
        self.driver.execute_script(js_command)
        #--------------Click on Create Customer button--------------------
        self.task_obj.get_Create_Customer_btn().click()
        time.sleep(10)

        #------------Create Project script----------------------------

        # ----------Click on add new button---------------
        self.task_obj.get_AddNew_button().click()
        time.sleep(5)
        # -----------click on New Project Option------------
        self.task_obj.get_options_from_dropdown('+ New Project',self.task_obj.get_Add_New_ddl(),self.task_obj.get_New_Project_option('+ New Project'))
        time.sleep(3)
        #-----------------Enter Project Name----------------------
        self.task_obj.get_Project_Name_txtbox().send_keys(data["TC001"]["ProjectName"])
        #-----------------Enter project description----------------------
        self.task_obj.get_Project_description().send_keys(data["TC001"]["ProjectDescription"])
        #-----------------Enter value to Task field------------------------
        self.task_obj.get_Task_txtbox().send_keys(data["TC001"]["TaskName"])
        #--------------Enter Task description-------------------------
        self.task_obj.get_Task_DesriptionIcon().click()
        self.task_obj.get_Task_DesriptionArea().send_keys(data["TC001"]["TaskDescription"])
        #------------------- Click on Save button ----------------------
        self.task_obj.get_SaveBtn().click()
        #--------------Enter Estimate-----------------
        self.task_obj.get_Estimate().send_keys(data["TC001"]["Estimate"])
        #-------------Click on Create Project button-----------------
        js_command='window.scroll(0,5000)'
        self.driver.execute_script(js_command)
        self.task_obj.get_CreateProjectButton().click()
        time.sleep(5)








