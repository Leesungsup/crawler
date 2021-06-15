import requests
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
url="https://www.transfermarkt.com/"
#정보요청
r=requests.get(url,headers=headers)
#상태확인
print(r.status_code)
