import PySimpleGUI as sg
import naver_search_crawling as cr
# PySimpleGUI 테마 설정
sg.theme('LightBlue')

# GUI 레이아웃 정의
layout = [
    # 상단: 검색어 입력창
    [sg.Text('상품명:'), sg.Input(key='-QUERY-', size=(40, 1)), sg.Button('검색')],

    # 가운데: 최저가 상품 정보 표시
    [sg.Text('최저가 제품명:', size=(15, 1)), sg.Text('', key='-LOW-NAME-', size=(50, 1))],
    [sg.Text('최저가 가격:', size=(15, 1)), sg.Text('', key='-LOW-PRICE-', size=(50, 1))],
    [sg.Text('판매몰 개수:', size=(15, 1)), sg.Text('', key='-LOW-SHOPS-', size=(50, 1))],

    # 하단: 전체 검색 결과 출력
    [sg.Text('검색 결과 목록:')],
    [sg.Multiline('', size=(80, 20), key='-RESULT-', disabled=True)]
]

# url = "https://danawa.com/?srsltid=AfmBOoqvhU5cdaTY0LMV-0Mn7lRFLf8woEOCvv1AOfMiLM34atgM5bp1"
# html = cr.web_get(url,"utf-8")
# text_list = cr.find_text_list(html,".search__input")
# price_list = cr.find_text_list(html,".prod_pricelist strong")
# print(price_list)

# 창 생성
window = sg.Window('다나와 최저가 검색기', layout)



# 이벤트 루프 (기능 없음, 화면 확인용)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == '검색':
        # 테스트용 예시 데이터
        url = "https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&tab=main"
        html = cr.web_get(url,"utf-8")
        
        name = cr.find_text_list(html,".prod_name")
        price = cr.find_text_list(html,".price_sect")
        shops = cr.find_text_list(html,"#productItem73614713")
        results = list(zip(name, price, shops))
        # 최저가 상품 추출
        cheapest = min(results, key=lambda x: x[1])
        window['-LOW-NAME-'].update(cheapest[0])
        window['-LOW-PRICE-'].update(f"{cheapest[1]}원")
        window['-LOW-SHOPS-'].update(f"{len(cheapest[2])}개 판매몰")

        # 전체 결과 목록 출력
        output = "\n".join([f"{name} / {price}원 / {shops}개 판매몰" for name, price, shops in results])
        window['-RESULT-'].update(output)

window.close()
