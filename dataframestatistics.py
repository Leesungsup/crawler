import requests
from bs4 import BeautifulSoup
import pandas as pd
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
url="https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
response=requests.get(url,headers=headers)
player_list=[]
if response.status_code==200:
    soup=BeautifulSoup(response.content,"html.parser")
    string=soup.find_all('tr',{'class':['even','odd']})
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
    #value=value[1:-1]#앞과 뒤를 짜름
    player_list.append([number,name,position,age,nation,team,value])
df=pd.DataFrame(player_list,columns=['number','name','position','age','nation','team','value'])
df['value']=df['value'].str.replace('€','')#column 데이터 일괄변경
df['value']=df['value'].str.replace('m','').astype('float')#column 데이터 일괄변경
#새로운 칼럼추가
df['시장가치(억)']=df['value']*13
print(df.head())
#칼럼 삭제
df.drop(columns=['value'],inplace=True)#inplace=True를 통해서 수정한 칼럼을 저장한다.
print(df.describe())#int와 float에 대한 평균 최소 최대값 출력
print(df['age'].mean())#칼럼에 평균출력
print(df['시장가치(억)'].sum())#columns의 합계 출력
print(df['nation'].mode())#columns의 가장 많이 나오는 데이터
print(df[df['nation']=='England'])
g=df.groupby('nation')
print(g.size())
print(g.count())
print(g.sum())
g=df.groupby('team')
print(g.sum())
print(g['시장가치(억)'].sum().sort_values())
