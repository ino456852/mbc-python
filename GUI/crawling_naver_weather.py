import requests               

# 1단계. requests
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&oquery=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&tqi=jurkidqVOswssLwBZBossssss7N-337673&ackey=xe2sm7tt"
response = requests.get(url)
html_text = response.text
# print(html_text)

# 2단계. BeautifulSoup4
from bs4 import BeautifulSoup as bs
soup = bs(html_text, 'html.parser')
temp = soup.select_one(".temperature_text").text # 현재온도
print(temp)