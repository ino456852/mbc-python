import requests               

# 1단계. requests
url = "https://news.naver.com/section/105"
response = requests.get(url)
html_text = response.text
# print(html_text)

# 2단계. BeautifulSoup4
from bs4 import BeautifulSoup as bs
soup = bs(html_text, 'html.parser')
news_header_list = soup.select("strong.sa_text_strong") # 현재온도
print("뉴스헤드갯수 = %s" % len(news_header_list))
for h in news_header_list:
    print(h.get_text)