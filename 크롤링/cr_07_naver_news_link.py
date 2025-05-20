import time
import requests

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_link_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        # result_list.append(tag.get("href")) # 1 a태그 뽑는법
        result_list.append(tag["href"]) # 2
    return result_list

def find_text(html_text, selector):
    from bs4 import BeautifulSoup as bs
    soup = bs(html_text, 'html.parser')
    return soup.select_one(selector).get_text()

if __name__ == "__main__":
    html = web_get("https://news.naver.com/section/105")
    # 뉴스링크 추철
    link_list = find_link_list(html, "a.sa_text_title")
    for link in link_list:
        print(link)
        link_html = web_get(link) #링크의 주소페이지 로딩
        # 링크된 페이지의 기사 제목
        link_title = find_text(link_html, "#title_area")
        print("기사제목 = %s" % link_title)
        import time
        time.sleep(1) # 1초쉼