from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.utils import create_driver
import json
import unittest

class TestLogin_A1234(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_page_obj=LoginPage(self.driver)
        self.home_page_obj=HomePage(self.driver)

    def tearDown(self):
        self.driver.close()


    def test_login_valid_TC001(self):
        data=json.load(open('./test/regression/login/A3_1234.json'))
        #go to login page
        self.login_page_obj.wait_for_login_page_load()
        #enter valid username
        self.login_page_obj.get_username_txtbox().send_keys(data['TC1234']['username'])
        self.login_page_obj.get_password_txtbox().send_keys(data['TC1234']['password'])
        self.login_page_obj.get_login_btn().click()

        #wait for home page to load and verify home page title
        self.home_page_obj.wait_for_home_page_load()
        expected_title=data['TC1234']['home_title']
        actual_title=self.driver.title
        assert expected_title == actual_title

        #click on logout button
        self.home_page_obj.get_logout_btn().click()

        # wait for login page to load and verify login page title
        self.login_page_obj.wait_for_login_page_load()
        expected_title=data['TC1234']['login_title']
        actual_title=self.driver.title
        assert expected_title == actual_title

