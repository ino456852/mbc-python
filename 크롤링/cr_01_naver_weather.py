#기본코드

def web_get(url):
    # requests 패키지 가져오기
    import requests               

    # 가져올 url 문자열로 입력

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    

    # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text
    return html_text # 함수끝

def find_text(html_text, selector):
    # BeautifulSoup 패키지 불러오기
    # 주로 bs로 이름을 간단히 만들어서 사용함
    from bs4 import BeautifulSoup as bs

    # html을 잘 정리된 형태로 변환
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

if __name__ == "__main__":
    html = web_get( 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&ackey=ki3g7cut' )
    t = find_text(html, ".temperature_text")
    print(t)
    
    r_list = find_text_list(html, ".week_item")
    for r in r_list:
        print(r)