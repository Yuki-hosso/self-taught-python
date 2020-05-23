import urllib.request
from bs4 import BeautifulSoup as BS

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BS(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            #print(url)
            if url is None:
                continue
            if 'atcl/contents/' in url:
                print(""+ url)


news = 'https://trendy.nikkeibp.co.jp/news/'

Scraper(news).scrape()