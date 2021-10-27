from selenium import webdriver
import requests
import time
import re
import random
from lxml import etree
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options,executable_path=r'D:\Users\Administrator\PycharmProjects\爬虫\刷csdn访问量\chromedriver.exe')
driver.get('https://www.dc10000.com/index/new_lg_search.html')
# driver.add_cookie("thinkphp_show_page_trace=0|0; thinkphp_show_page_trace=0|0; PHPSESSID=ajags0fvipgajvref3b4ornabo; Hm_lvt_afc2b8bbe5afca7b1c77c05445eadd98=1631958025; Hm_lpvt_afc2b8bbe5afca7b1c77c05445eadd98=1631958028")

time.sleep(2)
e=etree.HTML(driver.page_source)
urls=e.xpath('//div/a/@data-href')
for i in urls:
    driver.get('https://www.dc10000.com'+i)
    driver.find_element_by_xpath('//*[@id="page-detail-main"]/div[1]/div/div[1]/div[4]/div[2]').click()
    e = etree.HTML(driver.page_source)
    print(e.xpath('/html/body/div[23]/div/img/@src'))
    header = {'Referer': f'https://www.dc10000.com{i}',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

    url=e.xpath('//div/img/@src')
    print(url)
    time.sleep(10000)

temp = 0
while True:
    try:
        temp = driver.execute_script('return document.body.scrollHeight')
        js = "var q=document.documentElement.scrollTop="+str(temp)
        driver.execute_script(js)
        time.sleep(3)
        # dd=driver.find_element_by_class_name('ins-item')[-11:]
        # print(dd)
        data_hrefs=re.findall('data-href="(.+?)"',driver.page_source)
        print(data_hrefs)
        for i in data_hrefs:
            uu='https://www.dc10000.com'+i

            rr=requests.request("GET",url=uu)
            e=etree.HTML(rr.text)
            url=e.xpath('//img/@src')
            url_zhen=''
            for j in url:
                print(j)
                if "=" in j and "https" in j:
                    url_zhen=j
                    break
            print(3333)
            print(url_zhen)
            time.sleep(1000)
            if url_zhen not in sourc:
                sourc.append(url_zhen)
            else:
                continue
            with open(f'tupian/{str(time.time()).replace(".","")}.jpg','wb')as f:
                f.write(requests.get(url_zhen).content)
    except :
        print('111')
        time.sleep(1)