from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AddUser:
    def __init__(self,driver):
        self.driver=driver

    def get_User_tab(self):
        try:
            return self.driver.find_element_by_id('container_users')
        except:
            return None

    def get_New_User_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[contains(text(),'New User')]")
        except:
            return None

    def get_First_Name_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_firstNameField')
        except:
            return None

    def get_Last_Name_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_lastNameField')
        except:
            return None

    def get_Email_Id_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_emailField')
        except:
            return None

    def get_UserName_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_usernameField')
        except:
            return None

    def get_Password_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_passwordField')
        except:
            return None

    def get_ReType_Password_txtbox(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_passwordCopyField')
        except:
            return None

    def get_Department_dropdown(self):
        try:
            return self.driver.find_element_by_xpath("(//div[contains(text(),'department not assigned')])[1]")
        except:
            return None

    def get_Create_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='components_button submitBtn']")
        except:
            return None

    def wait_for_Create_User_page_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_First_Name_txtbox()))