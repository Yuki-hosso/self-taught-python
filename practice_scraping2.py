import requests
from bs4 import BeautifulSoup
 
r = requests.get("https://news.yahoo.co.jp/")
 
soup = BeautifulSoup(r.content, "html.parser")
 
# ニュース一覧を抽出
print("\n" + soup.find_all("div").text)