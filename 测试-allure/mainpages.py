import time

import allure
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from locations import OperationLocators,MainPageLogin

class BasePage(object):

    def __init__(self,driver:webdriver):
        self.tu = 'p_' + str(time.time()).replace('.', '') + '.png'
        self.driver=driver
        self.driver.implicitly_wait(10)

    def save_pic(self):

        self.driver.save_screenshot(self.tu)

    def return_driver(self):
        return self.driver

class MainPage(BasePage):

    def send_keys_ex(self,locate,key):
        ss=self.driver.find_element(*locate)
        ss.clear()
        ss.send_keys(key)

    @allure.feature('登陆orange')
    def login(self,account,pwd,url):
        self.driver.get(url)
        self.send_keys_ex(MainPageLogin.user_name,account)
        self.send_keys_ex(MainPageLogin.user_pwd,pwd)
        self.driver.find_element(*MainPageLogin.login_click).click()

    @allure.feature('添加用户')
    @allure.story('正常添加用户')
    @allure.story('详细添加用户')
    @allure.story('保存添加用户')
    def click_add(self):
        allure.step('点击人员')
        self.driver.find_element(*OperationLocators.pim_view).click()
        allure.step('点击添加')
        self.driver.find_element(*OperationLocators.add_user).click()

    @allure.feature('正常添加用户')
    def add_user(self,value):
        allure.step('输入姓名')
        self.send_keys_ex(OperationLocators.user_firstName,value['firstName'])
        allure.step('输入名字')
        self.send_keys_ex(OperationLocators.user_lastName,value['lastName'])
        if value['employeeId']:
            allure.step('输入员工id')
            self.send_keys_ex(OperationLocators.user_id,value['employeeId'])

    @allure.feature('详细添加用户')
    def add_user_details(self,value):
        self.add_user(value)
        self.driver.find_element(*OperationLocators.login_detail).click()
        self.save_pic()
        allure.attach.file(self.tu, attachment_type=allure.attachment_type.PNG)
        allure.step('点击创建登陆详情')
        if not self.driver.find_element(*OperationLocators.login_detail).is_selected():
            allure.step('点击创建登陆详情失败 再点一次')
            self.driver.find_element(*OperationLocators.login_detail).click()
        allure.step('输入用户名')
        self.send_keys_ex(OperationLocators.user_name,value['user_name'])
        allure.step('输入用户密码')
        self.send_keys_ex(OperationLocators.user_pwd,value['user_password'])
        allure.step('再次确认密码')
        self.send_keys_ex(OperationLocators.user_re_pwd,value['re_password'])
        allure.step('选择性别')
        Select(self.driver.find_element(*OperationLocators.user_status)).select_by_value(value['status'])


    @allure.feature('保存添加用户')
    def save_user(self):
        allure.step('点击保存')
        self.driver.find_element(*OperationLocators.save).click()
        self.save_pic()
        allure.attach.file(self.tu,attachment_type=allure.attachment_type.PNG)

