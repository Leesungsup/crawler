import requests
from bs4 import BeautifulSoup
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
url="https://www.transfermarkt.com/"
#정보요청
r=requests.get(url)
if r.status_code==200:
    html = response.text
    responce=BeautifulSoup(html,'html.parser')
    print(responce.find('p'))
else:
    print(r.status_code)
