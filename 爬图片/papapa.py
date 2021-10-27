import requests
import time
from lxml import etree
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    "referer":"https://www.dc10000.com"
}
req=requests.get('https://www.dc10000.com/index/new_sc_search.html',headers=header)
e=etree.HTML(req.text)

hrefs=e.xpath('/html/body/div[20]/div/div[1]/div[9]/a')

for i in hrefs:
    print(i)
    if "https" in i:
        r1=requests.get(i)
        # print(r1.text)
        time.sleep(10000)
