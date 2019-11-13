from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self,driver):
        self.driver=driver

    def get_logout_btn(self):
        try:
            return self.driver.find_element_by_xpath("//a[@id='logoutLink']")
        except:
            return None

    def wait_for_home_page_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_logout_btn()))