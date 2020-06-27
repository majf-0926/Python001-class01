# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装
import csv


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'

header = {
    'Cookie':'_csrf=5bbab77c8e48daaf66bd953b970b58f785f3df3f941ece3b40817a77417b03db; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593249963; uuid_n_v=v1; mojo-uuid=3b9f197abe06a36bfff61f53b4fd8a10; uuid=2952DE70B82C11EA80F64D80EBA969F715F44B208D524338B04EE4F115DFE71D; _lxsdk_cuid=172f3f880c9c8-02dfa45b259f3a-71415a3a-17ed82-172f3f880c9c8; __mta=141934477.1593231049375.1593248094060.1593249963303.6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593231046,1593248063; _lxsdk=2952DE70B82C11EA80F64D80EBA969F715F44B208D524338B04EE4F115DFE71D; _lxsdk_s=172f518e3a4-2e0-a9f-f74%7C%7C3; mojo-trace-id=2; mojo-session-id={"id":"f7415b85e1fb5b66b641653ab785f52b","time":1593249963157}',
    'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')
#print(bs_info)
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
#for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
    #for atag in tags.find_all('div'):
        #print(atag)
   # atag1=tags.find_all('div')
   # print("电影名称：")
    
    #atag2=tags.find('div').find('span',attrs={'class': 'hover-tag'})
    #if type(atag1[1]) != 'NoneType':
        #print(atag1[1].text)         
    # 获取电影类型
    #if type(atag1[3]) != 'NoneType':
        #print(atag1[3].text)    
    ## 获取上映时间
with open('movie.csv','w',newline='',encoding='utf-8') as f:
    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
        f_csv=csv.writer(f)
        atag1=tags.find_all('div')
        f_csv.writerow(["电影名称："])
        f_csv.writerow([atag1[0].find('span',attrs={'class': 'name'}).text])
        f_csv.writerow([atag1[1].text])
        f_csv.writerow([atag1[3].text])
    #csv_obj = open('data.csv', 'w', encoding="utf-8")


