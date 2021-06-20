import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
url="https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
response=requests.get(url,headers=headers)
player=[]
if response.status_code==200:
    soup=BeautifulSoup(response.content,'html.parser')
    string=soup.find_all('tr',{'class':['odd','even']})
else:
    print(response.status_code)
for info in string:
    information=info.find_all('td')
    number=information[0].get_text()
    name=information[3].get_text()
    position=information[4].get_text()
    #age=information[5].get_text()#문자
    age=int(information[5].get_text())#숫자로 변환
    nation=information[6].img['alt']
    team=information[7].img['alt']
    #value=information[8].span['title']
    value=information[8].get_text()
    player.append([number,name,position,age,nation,team,value])
df=pd.DataFrame(player,columns=['number','name','position','age','nation','team','value'])
#print(df)
#print(pd.read_csv('./transfermarket1~25.csv'))
(row,colum)=df.shape
print(row,colum)
print(df.info())
print(df.head(1),df.tail(1))
print(df[0:3])
print(df['name'].head())
print(df[['name','value']].tail())
print(df.loc[0:2])
print(df.loc[0,'name'])
print(df.loc[0:4],['name','team','value'])
k=[]
k=df[df['age']<=20]
print(k)
print(df[df['team']=='Tottenham Hotspur'])
print(df.loc[df['age']>=30,['name','value']])
#print(pd.read_csv('https://github.com/Leesungsup/crawler/blob/main/transfermarket1~25.csv',error_bad_lines=False))
#df.to_csv("transfermarket1~25.csv",index=False)
