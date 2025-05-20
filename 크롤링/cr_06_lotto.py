import requests

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding != "":
        response.encoding = encoding
    html_text = response.text
    return html_text

def find_text_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get_text())
    return result_list

def find_link_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get("href")) # 1 a태그 뽑는법
        # result_list.append(tag["href"]) # 2
    return result_list

def find_src_list(html_text, selector):
    from bs4 import BeautifulSoup as bs
    # html을 잘 정리된 형태로 변환
    soup = bs(html_text, 'html.parser')
    tag_list = soup.select(selector)
    
    result_list = []
    for tag in tag_list:
        result_list.append(tag.get("src"))
    return result_list



if __name__ == "__main__":
    html = web_get("https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1")
    # src_list = find_src_list(html, ".current_result .ball") 
    # for src in src_list:
    #     print(src)
    
    title_list = find_text_list(html, ".nums")
    for t in title_list:
        print(t)
        
    # 링크 리스트 추출
    # link_list = find_link_list(html, ".current_result img")
    # for t in link_list:
    #     print(t)