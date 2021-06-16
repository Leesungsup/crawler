import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]
for i in range(1,3):
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
    url=f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page={i}"
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.content,'html.parser')
        string=soup.find_all('tr',{'class':['odd','even']})
    else:
        print(response.status_code)
    for info in string:
        information=info.find_all('td')
        number.append(information[0].get_text())
        name.append(information[3].get_text())
        position.append(information[4].get_text())
        age.append(information[5].get_text())
        nation.append(information[6].img['alt'])
        team.append(information[7].img['alt'])
        value.append(information[8].span['title'])
    df=pd.DataFrame({
    'number':number,
    'name':name,
    'position':position,
    'age':age,
    'nation':nation,
    'team':team,
    'value':value,
    })
print(df)
df.to_csv("transfermarket1~25.csv",index=False)
