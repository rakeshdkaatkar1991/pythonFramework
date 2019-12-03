from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TaskPage:
    def __init__(self,driver):
        self.driver=driver

    def get_Tasks_tab(self):
        try:
            return self.driver.find_element_by_id('container_tasks')
        except:
            return None

    def get_AddNew_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='title ellipsis']")
        except:
            return None

    def get_New_Customer_option(self,RequiredValue):
        try:
            #return self.driver.find_element_by_xpath("//div[@class='item createNewCustomer']")
            return self.driver.find_element_by_xpath("//div[@class='item createNewCustomer'][text()='"+RequiredValue+"']")
        except:
            return None

    def get_New_Project_option(self,RequiredValue):
        try:
            return self.driver.find_element_by_xpath("//div[@class='item createNewProject'][text()='"+RequiredValue+"']")
        except:
            return None
    def get_Customer_Name_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='inputFieldWithPlaceholder newNameField inputNameField']")
        except:
            return None

    def get_Project_Name_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='projectNameField inputFieldWithPlaceholder inputNameField']")
        except:
            return None

    def get_Project_description(self):
        try:
            return self.driver.find_element_by_xpath("//textarea[@placeholder='Add Project Description']")
        except:
            return None

    def get_Customer_Description_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//textarea[@placeholder='Enter Customer Description']")
        except:
            return None

    def get_Customer_drpdown(self):
        try:
            #return self.driver.find_element_by_xpath("//div[@class='emptySelection']")
            return self.driver.find_element_by_xpath("//span[@class='customerSelectorPlaceholder selectorWithPlaceholderContainer']//div[@class='dropdownButton']")

        except:
            return None

    def get_Cust_dropdown_list(self):
        try:
            return self.driver.find_elements_by_xpath("//span[@class='customerSelectorPlaceholder selectorWithPlaceholderContainer']//div[@class='scrollableContainer ']")
            #return self.driver.find_elements_by_xpath("//div[@class='searchItemList'][@style='display: block;']")
        except:
            return None

    def get_Required_Project_option(self,requiredValue):
        try:
            return self.driver.find_element_by_xpath("//div[@class='itemRow cpItemRow '][text()='"+requiredValue+"']")
        except:
           return None

    def get_Create_Customer_btn(self):
        try:
            #return self.driver.find_element_by_xpath("//div[@class='components_button  withPlusIcon']")
            return self.driver.find_element_by_xpath("//div[text() = '  Create Customer']")
        except:
            return None

    def get_Add_New_ddl(self):
        try:
            return self.driver.find_elements_by_xpath("//div[@class='dropdownContainer addNewMenu']")
        except:
            return None

    def get_Project_Name_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='projectNameField inputFieldWithPlaceholder inputNameField']")
        except:
            return None

    def get_Task_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@placeholder='Enter task name'])[1]")
        except:
            return None

    def get_Task_DesriptionIcon(self):
        try:
            return self.driver.find_element_by_xpath("(//a[@id='descriptionElement'])[1]")
        except:
            return None

    def get_Task_DesriptionArea(self):
        try:
            return self.driver.find_element_by_xpath("//textarea[@id='editDescriptionPopupText']")
        except:
            return None

    def get_SaveBtn(self):
        try:
            return self.driver.find_element_by_xpath("//input[@id='scbutton']")
        except:
            return None

    def get_Estimate(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@placeholder='not needed'])[1]")
        except:
            return None

    def get_CreateProjectButton(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='  Create Project']")
        except:
            return None

    def get_SearchField(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@placeholder='Start typing name ...'])[1]")
        except:
            return None

    def get_TaskCheckBox(self):
        try:
            #return self.driver.find_element_by_xpath("//div[text()='"+TaskName+"']/../../../../../td")
            return self.driver.find_element_by_xpath("//div[@class='checkbox inactive' and @style='display: flex;']")
        except:
            return None

    def get_ViewProjectLink(self,ProjectName):
        try:
            return self.driver.find_element_by_xpath("//div[text()='"+ProjectName+"']")
        except:
            return None

    def get_AssignToLink(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Assign to']")
        except:
            return None

    def get_AssignButton(self):
        try:
            return self.driver.find_element_by_xpath("(//div[@class='withIcon submitBtn greyButton'])[1]")
        except:
            return None

    def wait_for_Create_New_Customer_Page_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_Customer_Name_txtbox()))

    def wait_for_Add_new_btn_to_be_displayed(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_AddNew_button()))


#----------Method to load dropdown contents in to list and select required dropdown option from list--------------------------------
    def get_options_from_dropdown(self,requiredValue,element_list,element_to_Click):
        listOptions=element_list
        new_list=listOptions[0].text.split('\n')
        size=len(new_list)
        for i in range(0,size):
            text=new_list[i]
            if text==requiredValue:
                element_to_Click.click()
                break
        else:
            print("Element not found in drop down list ")










