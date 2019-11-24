from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from test.regression.add_user import test_UserValidation_A_5678

class User:
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
            return self.driver.find_element_by_xpath("//div[@class='userGroupRow_userPanel']//div[@class='selector']//*[@class='downIcon']")
        except:
            return None

    def get_ddl_values(self):
        try:
            return self.driver.find_elements_by_xpath("//div[@class='itemsContainer']/div")
        except:
            return None

    def get_Create_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='buttonsBox']/div[contains(text(),'Create User')]")
        except:
            return None

    def get_Search_icon(self):
        try:
            return self.driver.find_element_by_xpath("//th[@class='controlsPlaceholder userName secondLayer']//div[@class='icon']")
        except:
            return None

    def get_Search_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='inputPlaceholder animShowWordsField']//input[@placeholder='Start typing name...']")
        except:
            return None

    def get_Actiplans_Togglebtn(self):
        try:
            return self.driver.find_element_by_id('createUserPanel_accessToOtherProductSelectorPlaceholder')
        except:
            return None

    def get_SearchedName_link(self,enteredUserName):
        try:
            return self.driver.find_element_by_xpath("//span[@class='userNameSpan']/span[text()='"+enteredUserName+"']")
        except:
            return None

    def get_Delete_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='deleteButton actionButton']")
        except:
            return None

    def get_User_not_found_Message(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='noFoundUsersMessage']")
        except:
            return None

    def get_Time_Track_link(self):
        try:
            return self.driver.find_element_by_id('container_tt')
        except:
            return None

    def get_First_User_cell(self,UserName):
        try:
            return self.driver.find_element_by_xpath("//span[contains(text(),'"+UserName+"')]")
        except TimeoutError:
            return  None


    def wait_for_Create_User_page_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_First_Name_txtbox()))

    def wait_for_dept_ddlValues_to_Load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.staleness_of(self.get_ddl_values()))

    def wait_for_create_button_to_click(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Create User')]")))

    def wait_for_Search_icon(self):
        wait=WebDriverWait(self.driver,50)
        wait.until(expected_conditions.visibility_of(self.get_Search_icon()))