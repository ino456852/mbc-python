import requests
from bs4 import BeautifulSoup

# 네이버 날씨 페이지 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=skfTl&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8&ackey=omp3au61"

# HTTP 요청
response = requests.get(url)

# print(response.text)

# HTML을 파싱하기 위해 BeautifulSoup 사용
soup = BeautifulSoup(response.text, 'html.parser')

# result = soup.find(태그명, attrs={속성명:속성값}) 조건에 해당하는 첫번째 태그만 추출
# result = soup.find_all() 조건에 해당하는 모든 태그 추출

# result = soup.select_one("선택자") 선택자에 해당하는 첫번째 태그
# result = soup.select("선택자") 선택자에 해당하는 모든 태그
# 여러개 가져올 경우 
# for t in result:
#   print(t.get_text())
# 
# 태그.string 선택된 태그의 글자
# 태그.text, get_text() 선택된 태그의 하위자손까지의 text
# 
# 속성추출: 태그명["속성명"] 또는 태그명.attrs["속성명"]
# 

# temp = soup.select_one("div.temperature_text").get_text()
# print(temp)
temp2 = soup.select_one("div.temperature_info").get_text()
print(temp2)