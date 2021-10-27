import pytest
from selenium import webdriver
import yaml

from mainpages import MainPage
from read_yaml import read_yaml



class Test_Orange():


    @classmethod
    def get_login_infos(self):
        return yaml.safe_load(open('login_infos.yaml'))

    @pytest.fixture(scope='session', autouse=True)
    def open_login(self):
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.mp=MainPage(self.driver)
        info=self.get_login_infos()
        print(info[0])
        self.mp.login(info[0]['username'],info[0]['password'],info[0]['url'])
        yield self.mp
        self.driver.close()

    # @pytest.fixture(scope='module', autouse=True)
    # def query_param(request):
    #     return request.param

    @pytest.mark.parametrize('value',read_yaml('test.yaml'))
    def test_adduser(self,value,open_login):
        open_login.click_add()
        open_login.add_user(value)
        open_login.save_user()
        assert value['result'] in open_login.return_driver().current_url

    @pytest.mark.parametrize('value', read_yaml('test_details.yaml'))
    def test_adduser_details(self,value,open_login):
        open_login.click_add()
        open_login.add_user_details(value)
        open_login.save_user()
        assert value['result'] in open_login.return_driver().current_url




if __name__ == '__main__':

    pytest.main()



