import requests               
# 1단계. requests
url = "https://news.daum.net/tech"
response = requests.get(url)
response.encoding = 'utf-8'
html_text = response.text
# print(html_text)

# 2단계. BeautifulSoup4
from bs4 import BeautifulSoup as bs
soup = bs(html_text, 'html.parser')
news_list = soup.select("ul.list_newsheadline2 li") # 뉴스기사 별 태그
print("뉴스갯수 = %s" % len(news_list))
for news in news_list:
    # # 제목만 추출
    # title = news.select_one("strong.sa_text_strong").get_text()
    # # print(title)
    
    # # 원본 기사 링크 추출
    # href = news.select_one("a.sa_text_title").attrs["href"]
    # # print(href)
    
    # # 신문사 이름 추출, 출력
    # info = news.select_one("div.sa_text_press").get_text() # 네이버 신문사 이름
    # print(info)
    
    # 다음 뉴스
    # 기사제목
    title = news.select_one("strong.tit_txt").get_text()
    print(title)
    
    # 기사 내용
    desc  = news.select_one("strong.desc_txt")
    if desc :
        print(desc .get_text())
    else:
        print("요약 없음")  # 또는 그냥 pass

    
    # 신문사 이름
    span = news.select_one("span.con_txt").get_text()
    print(span)
    