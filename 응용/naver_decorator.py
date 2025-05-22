def web_get(url,encoding=""):
    import requests               
    response = requests.get(url)
    if encoding:  # encoding 인자가 주어졌다면 강제로 설정
        response.encoding = encoding    
    html_text = response.text
    return html_text # 함수끝

def find_text(html_text, selector):
    from bs4 import BeautifulSoup as bs
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

def find_text_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

def naver_weather( target_func ):
    def wrapper(city):
        html = web_get( 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%s&ackey=ki3g7cut' % ("날씨 "+city) )
        temp = find_text(html, ".temperature_text")
        weather = find_text(html, ".weather")
        target_func(temp=temp, weather=weather)
    return wrapper

def daum_news_list( news_func ):
    def wrapper():
        html = web_get( 'https://news.daum.net/tech', encoding="utf-8")
        news_list = find_text_list(html, ".list_newsheadline2 .tit_txt, .list_newsblock .tit_txt")
        news_func(news_list)
    return wrapper

@daum_news_list
def print_news(news_list=""):
    print("뉴스 리스트:%s" % news_list)
    
@naver_weather
def print_weather(city="서울", temp="", weather=""):
    print("온도:%s" % temp)
    print("날씨: %s" % weather)

if __name__ == "__main__":
    # html = web_get( 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&ackey=ki3g7cut' )
    # t = find_text(html, ".temperature_text")
    # print(t)
    # t = find_text(html, ".weather")
    # print(t)
    # print_weather("해남")
    print_news()