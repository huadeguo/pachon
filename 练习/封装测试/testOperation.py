from selenium import webdriver
import unittest
from ddt import ddt,file_data
from BeautifulReport import BeautifulReport as bf
from mainpage import MainPage



@ddt
class Test_Orange(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'D:\Users\Administrator\PycharmProjects\爬虫\刷csdn访问量\chromedriver.exe')
        # cls.driver = webdriver.Firefox(executable_path=r'D:\Users\Administrator\PycharmProjects\爬虫\练习\geckodriver.exe')
        cls.mp=MainPage(cls.driver)
        cls.mp.login('admin','Bitnami.12345')
        assert 'admin' in cls.driver.page_source

    def setUp(self):
        self.mp.click_add()

    @file_data(r'D:\Users\Administrator\PycharmProjects\爬虫\练习\封装测试\test.yaml')
    def test_adduser(self,**value):
        self.mp.add_user(**value)
        self.mp.save_user()
        assert '/symfony/web/index.php/pim/viewPersonalDetails/empNumber' in self.driver.current_url

    @file_data(r'D:\Users\Administrator\PycharmProjects\爬虫\练习\封装测试\test_details.yaml')
    def test_adduser_details(self,**value):
        self.mp.add_user_details(**value)
        self.mp.save_user()
        assert '/symfony/web/index.php/pim/viewPersonalDetails/empNumber' in self.driver.current_url

    def tearDownClass(cls):
        print('操作结束')
        cls.driver.close()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Orange))
    runner = bf(suit)
    runner.report(filename='report111', description='测试')



