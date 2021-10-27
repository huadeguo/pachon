import requests
from threading import Thread
from threading import Semaphore
import re
import time
import random
from lxml.etree import HTML
import os
#请求头
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    "cookie":"_uuid=A7AAA3A0-FE0F-697C-7671-DFCE10DD5E2250066infoc; buvid3=574C033A-400B-4EF3-8045-F1E620D74E5F167638infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(JY)J))lY)k0J'uYJ|uRRYJ); fingerprint=188b02b3873ebe888c6e474851ea1246; buvid_fp=574C033A-400B-4EF3-8045-F1E620D74E5F167638infoc; buvid_fp_plain=574C033A-400B-4EF3-8045-F1E620D74E5F167638infoc; DedeUserID=392064318; DedeUserID__ckMd5=d7e667fb8ca547a5; SESSDATA=476c88b5%2C1645696684%2C25c78*81; bili_jct=f4a06b08cc91e7a05c10c63d8f4ac03e; bp_video_offset_392064318=562704324245930145; CURRENT_QUALITY=80; bsource=search_bing; sid=asecq6dj; innersign=1; PVID=2; bfe_id=1bad38f44e358ca77469025e0405c4a6",
    "referer":"https://www.bilibili.com/video/BV1Ht411C7wp?from=search&seid=16753236418743225922&spm_id_from=333.337.0.0"
}
def paqu(name,i,sem:Semaphore):
    sem.acquire()
    rr=requests.get(i,headers=header)
    e=HTML(rr.text)
    url=e.xpath('/html/head/script[5]/text()')
    print(url)
    #获取视频真实地址
    url_video=re.findall('video":\[{"id":\d+,"baseUrl":"(.+?)"',url[0])
    #获取音频真实地址
    url_audio=re.findall('audio":\[{"id":\d+,"baseUrl":"(.+?)"',url[0])
    print(url_video)
    print(url_audio)

    path1='shipin/'+str(name)+'.mp4'
    with open('shipin/'+str(name)+'.mp4','wb')as f:
        r1=requests.get(url_video[0], headers=header)
        print(r1.status_code)
        f.write(r1.content)
    path2='shipin/'+str(name)+'.mp3'
    with open('shipin/'+str(name)+'.mp3','wb')as f:
        f.write(requests.get(url_audio[0], headers=header).content)
    path3='shipin/'+str(name)+'合成.mp4'
    # 利用插件ffmpeg组合音频和视频
    os.system(f"ffmpeg -i {path1} -i {path2} -c copy {path3}")
    os.remove(path1)
    os.remove(path2)
    time.sleep(random.randint(1,3))
    sem.release()

#搜索请求
def sousuo(sou):
    dt={}
    req=requests.get(f'https://search.bilibili.com/all?keyword={sou}&from_source=web_search')
    #正则过滤搜索结果所有视频的url
    urls=re.findall(r'href="//(www.+search?)" title',req.text)
    for name,i in enumerate(urls):
        dt[name]='http://'+i
    return dt
# sousuo('搞笑')
# paqu('123','https://www.bilibili.com/video/BV18v411w7PD?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.6')
if __name__ == '__main__':
    sem=Semaphore(5)
    result=sousuo('舞蹈')
    for i,j in result.items():
        print(i,j)
        Thread(target=paqu,args=(i,j,sem)).start()