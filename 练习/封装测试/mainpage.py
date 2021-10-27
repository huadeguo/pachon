from locators import OperationLocators,MainPageLogin
import time
from selenium.webdriver.support.ui import Select



class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(3)

class MainPage(BasePage):

    def login(self,account,pwd,url):
        self.driver.get(url)
        self.driver.find_element(*MainPageLogin.user_name).send_keys(account)
        self.driver.find_element(*MainPageLogin.user_pwd).send_keys(pwd)
        self.driver.find_element(*MainPageLogin.login_click).click()

    def click_add(self):
        self.driver.find_element(*OperationLocators.pim_view).click()
        self.driver.find_element(*OperationLocators.add_user).click()

    def add_user(self,value):

        self.driver.find_element(*OperationLocators.user_firstName).send_keys(value['firstName'])
        self.driver.find_element(*OperationLocators.user_lastName).send_keys(value['lastName'])
        if value['employeeId']:
            self.driver.find_element(*OperationLocators.user_id).clear()
            self.driver.find_element(*OperationLocators.user_id).send_keys(value['employeeId'])

    def add_user_details(self,value):
        self.add_user(value)
        self.driver.find_element(*OperationLocators.login_detail).click()
        self.driver.find_element(*OperationLocators.user_name).send_keys(value['user_name'])
        self.driver.find_element(*OperationLocators.user_pwd).send_keys(value['user_password'])
        self.driver.find_element(*OperationLocators.user_re_pwd).send_keys(value['re_password'])
        Select(self.driver.find_element(*OperationLocators.user_status)).select_by_value(value['status'])
        self.driver.find_element(*OperationLocators.save).click()

    def save_user(self):
        self.driver.find_element(*OperationLocators.save).click()



