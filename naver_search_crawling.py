import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs


def get_browser(url, auto_close=True):
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    if not auto_close:
        # 브라우저 꺼짐 방지 옵션
        chrome_options.add_experimental_option("detach", True)
        # 크롬드라이버 실행
    driver = webdriver.Chrome(options=chrome_options)
    # 크롬 드라이버에 url 주소 넣고 실행
    driver.get(url)
    return driver  # 웹브라우저 컨트롤 객체


def web_get(url, encoding=""):
    response = requests.get(url,
                            cookies={"NNB": ''},
                            headers={
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
                            })
    if encoding != "":
        response.encoding = encoding  # 유니코드로 인코딩
    html_text = response.text
    print("cookies = %s" % response.cookies.get_dict())
    return html_text  # 함수끝


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
        result_list.append(tag.get_text().strip())
    return result_list
    # 속성값 추출기능


# def find_attr_list(html_text, selector, attr_name):
#     from bs4 import BeautifulSoup as bs
#     # html을 잘 정리된 형태로 변환
#     soup = bs(html_text, 'html.parser')
#     tag_list = soup.select(selector)
#     result_list = []
#     for tag in tag_list:
#         result_list.append(tag.attrs[attr_name])
#     return result_list


def main():
    # url="https://pcmap.place.naver.com/restaurant/list?query=종로구%20분식집&x=127.00428990000347&y=37.581292900000975&clientX=126.990262&clientY=37.574461&bounds=126.99546006792906%3B37.57489875856497%3B127.00464395159503%3B37.587516457086906&display=70&ts=1747965556712&additionalHeight=76&locale=ko&mapUrl=https%3A%2F%2Fmap.naver.com%2Fp%2Fsearch%2F종로구%20분식집"
    # 메인페이지 검색결과 "종로구 분식집"
    # url="http://naver.com"
    # html = web_get(url, encoding="utf-8")
    # url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=종로구 분식집"
    # url = "https://www.melon.com/chart/index.htm"
    # 전체 HTML 추출

    

    menu_url = "https://www.melon.com/chart/index.htm"
    driver = get_browser(menu_url, False)
    html = driver.page_source
    # soup = bs(html, "html.parser")
    html = web_get(menu_url, encoding="utf-8")
    play_list_rank = find_text_list(html, "tbody .rank ")
    play_list_title = find_text_list(html, ".ellipsis.rank01")
    play_list_name = find_text_list(html, ".ellipsis.rank02")
    print(play_list_rank,play_list_title,play_list_name)
    
    # print("갯수=%s" % len(play_list_rank,play_list_title))
    # 가게 id 목록
    # shop_id_list = find_attr_list(html, "li.UEzoS", "data-nmb_res-doc-id")
    # print("갯수=%s" % len(shop_id_list))
    # print(shop_id_list)
    # 메뉴 리스트
    # url="https://pcmap.place.naver.com/restaurant/%s/menu/list" % shop_id_list[0]
    # menu_url = f"https://pcmap.place.naver.com/restaurant/{shop_id_list[5]}/menu/list?entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202505231045&locale=ko&svcName=map_pcv5&searchText=%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EB%B6%84%EC%8B%9D%EC%A7%91"
    # time.sleep(2)
    # 동적 생성된 페이지 소스를 추출
    # html = driver.page_source
    # menu_list = find_text_list(html, ".lPzHi")  # 메뉴이름
    # # print( "menu_list 갯수=%s" % len(menu_list) )
    # # print(menu_list)
    # 실습 : 메뉴 이름과 가격 출력
    # price_list = find_text_list(html, ".GXS1X em")
    # menu_price = list(zip(menu_list, price_list))
    # print(menu_price)
    # for menu, price in zip(menu_list, price_list):
    #     print( f"price_list 가격 = {menu},{price} 원" )
    # print(price_list)


    # # url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%A2%85%EB%A1%9C%EA%B5%AC+%EB%B6%84%EC%8B%9D%EC%A7%91&tqi=ju%2FZRwpzLi0ssBKIzjZssssstwG-296923&ackey=o8whzhhy"
    # url="https://pcmap.place.naver.com/restaurant/list?query=%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EB%B6%84%EC%8B%9D%EC%A7%91&x=126.990262&y=37.574461&clientX=126.990262&clientY=37.574461&from=nx&fromNxList=true&abt=%5B%7B%22eid%22%3A%22PWL-PND-PLC%22%2C%22value%22%3A%7B%22bucket%22%3A%222%22%2C%22is_control%22%3Afalse%7D%7D%5D&bucket=2&bucketId=PWL-PND-PLC&x=126.990262&y=37.574461&entry=pll&display=70&ts=1747963293646&additionalHeight=76&locale=ko&mapUrl=https%3A%2F%2Fmap.naver.com%2Fp%2Fsearch%2F%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EB%B6%84%EC%8B%9D%EC%A7%91"
    # driver = get_browser(url)
    # time.sleep(2)
    # #동적 생성된 페이지 소스를 추출
    # html = driver.page_source
    # # print(html.find("TYaxT"))
    # shop_name_list = find_text_list(html, "span.TYaxT")
    # print( "갯수=%s" % len(shop_name_list) )
    # print(shop_name_list)
    # #메뉴추출
    # menu_url="https://pcmap.place.naver.com/restaurant/31202565/menu/list?entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202505231045&locale=ko&svcName=map_pcv5&searchText=%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EB%B6%84%EC%8B%9D%EC%A7%91"
    # driver = get_browser(menu_url)
    # time.sleep(2)
    # #동적 생성된 페이지 소스를 추출
    # html = driver.page_source
    # menu_list = find_text_list(html, ".lPzHi") #메뉴이름
    # print( "menu_list 갯수=%s" % len(menu_list) )
    # print(menu_list)
if __name__ == "__main__":
    main()
