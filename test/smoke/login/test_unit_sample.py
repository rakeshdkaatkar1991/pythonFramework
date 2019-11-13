import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestUnitSample(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_obj=LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_unit_sample(self):
        self.login_obj.wait_for_page_load()
        self.login_obj.get_username_txtbox().send_keys("Invalid")
        self.login_obj.get_password_txtbox().send_keys("Invalid")
        self.login_obj.get_login_btn().click()
        actual_err_msg=self.login_obj.get_login_err_msg().text
        expected_err_msg="Username or Password is invalid. Please try again."
        assert actual_err_msg==expected_err_msg