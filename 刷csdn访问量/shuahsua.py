from selenium import webdriver
import requests
import time
for i in range(100):
    options = webdriver.ChromeOptions()
    # url=requests.get('http://127.0.0.1:5555/').text
    # print(url)
    # options.add_argument(f"--proxy-server=http://{url}")
    # options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    driver=webdriver.Chrome(chrome_options=options,executable_path=r'D:\Users\Administrator\PycharmProjects\爬虫\刷csdn访问量\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://blog.csdn.net/qq_44727974/article/details/120321161?spm=1001.2014.3001.5501')
    driver.delete_all_cookies()
    time.sleep(2)
    temp=driver.execute_script('return document.body.scrollHeight')
    j=0
    while j<temp:
        j += 20
        js = "var q=document.documentElement.scrollTop="+str(j)
        driver.execute_script(js)
        time.sleep(0.1)
    driver.close()