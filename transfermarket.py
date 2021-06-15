import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
url="https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
response=requests.get(url,headers=headers)
number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]
number1=[]
name1=[]
position1=[]
age1=[]
nation1=[]
team1=[]
value1=[]
if response.status_code==200:
    soup=BeautifulSoup(response.content,'html.parser')
    string=soup.find_all('tr',{'class':['odd','even']})
    print(len(string))
    print(string[0])
    print(string[1])
for info in string:
    information=info.find_all('td')
    print(information)
    #tag까지
    number1.append(information[0])
    print(number1)
    #안의 내용만
    number.append(information[0].get_text())
    print(number)

else:
    print(response.status_code)
