import requests
from bs4 import BeautifulSoup
from datetime import datetime

def make_rss():
    ua = "Mozilla/5.0"
    url = "https://www.thepaper.cn/newsList"
    res = requests.get(url, headers={"User-Agent":ua})
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.find_all("div", class_="news_item")

    rss = f'<?xml version="1.0" encoding="utf-8"?>\n<rss version="2.0">\n<channel>\n<title>澎湃新闻</title>\n<link>{url}</link>\n<lastBuildDate>{datetime.now()}</lastBuildDate>\n'
    for i in items[:20]:
        try:
            tit = i.find("h2").get_text(strip=True)
            lk = "https://www.thepaper.cn" + i.find("a")["href"]
            txt = i.find("p").get_text(strip=True)
            rss += f'<item><title>{tit}</title><link>{lk}</link><description>{txt}</description></item>\n'
        except:
            continue
    rss += '</channel>\n</rss>'
    with open("pengpai.xml","w",encoding="utf-8") as f:
        f.write(rss)
    print("生成完成 pengpai.xml")

if __name__=="__main__":
    make_rss()
