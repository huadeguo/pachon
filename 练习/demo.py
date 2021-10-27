from selenium import webdriver
import requests
from random import randint
ip='121.36.224.237:3000'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
email=f"191${randint(1111,9999)}@juice"
password="123123"
json_data_regist={"email":email,"password":password,"passwordRepeat":"123123","securityQuestion":{"id":5,"question":"Maternal grandmother's first name?","createdAt":"2021-09-24T06:32:50.413Z","updatedAt":"2021-09-24T06:32:50.413Z"},"securityAnswer":"123123"}
req=requests.post(f'http://{ip}/api/Users/',json=json_data_regist)
driver=webdriver.Chrome(r'D:\Users\Administrator\PycharmProjects\爬虫\刷csdn访问量\chromedriver.exe')
url='http://'+ip+'/#/login'
driver.get(url)
# WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(By.ID,'kw'))
driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginButton"]').click()
driver.switch_to_window(driver.window_handles[-1])
driver.implicitly_wait(100)
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[1]/figure/mat-card/div[1]').click()
driver.find_element_by_xpath('//*[@id="mat-expansion-panel-header-0"]').click()
dd=driver.find_element_by_xpath('//*[@id="cdk-accordion-child-0"]/div/div/div/div/div[2]/button')
for i in range(100):
    dd.click()
