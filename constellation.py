#星座爬蟲
#以科技紫微網的星座運勢為目標

#使用requests, BeautifulSoup
import requests
from bs4 import BeautifulSoup

def star_crawler(star_num):
    session = requests.Session()
	
    #headers為避免被認定成機器人的措施
    html_doc = session.get("http://astro.click108.com.tw/daily_0.php?iAstro="+star_num, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }).text 
    starmsg = ""
    soup = BeautifulSoup(html_doc, 'html.parser')
    data = soup.find("div", class_="TODAY_CONTENT")
    starmsg+=data.find("h3").getText() + "\n"
	
    #只顯示文字內容
    for d in data.findAll("p"):
        starmsg+=d.getText() + "\n"
        pass
    return starmsg
    pass

#括弧內放星座順序：
#牡羊0, 金牛1, 雙子2, 巨蟹3, 獅子4, 處女5,
#天秤6, 天蠍7, 射手8, 魔羯9, 水瓶10, 雙魚11
message=star_crawler("0")

print(message)