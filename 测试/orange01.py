from selenium import webdriver
import unittest
import random
import time
from HTMLTestRunner import HTMLTestRunner
from ddt import ddt
from ddt import file_data
from selenium.webdriver.common.keys import Keys

@ddt
class Test_Orange01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始了')
        cls.driver = webdriver.Chrome(executable_path=r'D:\Users\Administrator\PycharmProjects\爬虫\刷csdn访问量\chromedriver.exe')
        cls.driver.get('http://120.78.193.32:8080')
        cls.driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('admin')
        cls.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('Bitnami.12345')
        cls.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

    @file_data('职位.yaml')
    def test_login(self,**value):
        self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="menu_admin_viewJobTitleList"]').click()
        self.driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
        self.driver.find_element_by_xpath('//*[@id="jobTitle_jobTitle"]').send_keys(value['name'])
        self.driver.find_element_by_xpath('//*[@id="jobTitle_jobDescription"]').send_keys(value['describe'])
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        # print(driver.page_source)
        # assert 'admin' in self.driver.page_source
    @classmethod
    def tearDownClass(cls):
        print('操作结束')
        cls.driver.close()

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Orange01))
    with open('result.html','wb') as f :
        runner=HTMLTestRunner(stream=f,title='测试报告',description='自动化测试')
        runner.run(suite)