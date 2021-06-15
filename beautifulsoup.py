import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    string=soup.find('a').get_text()
    print(string)
    string=soup.find_all('a')
    print(string)
    print(string[0])
    for i in string:
        print(i['href'])
    for i in string:
        print(i.get_text())
    string=soup.find_all('a',class_="sister")
    print(string)
    string=soup.find_all('a',{'class':'sister'})
    print(string)
    string=soup.find_all('a',id="link3")
    print(string)
    string=soup.find_all('a',{'id':'link3'})
    print(string)


else :
    print(response.status_code)
