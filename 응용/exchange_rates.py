import PySimpleGUI as sg

sg.theme('LightBlue')

layout = [
    
    # 상단: 금액 입력 + 통화 선택
    [sg.Text('금액 입력:'), sg.Input(key='-AMOUNT-', size=(15,1)), 
     sg.Text('통화 선택:'), sg.Combo(['USD', 'EUR', 'JPY 100', 'CNY', 'KRW'], default_value='USD', key='-CURRENCY-', readonly=True)],
    [sg.Button('계산하기')],

    # 중간: 변환 결과 표시
    [sg.Text('계산 결과:', font=('Arial', 14))],
    [sg.Text('', size=(30, 1), key='-RESULT-', font=('Arial', 14))],

    # 하단: 주요 통화의 현재 환율 리스트
    [sg.Text('📌 주요 통화 환율 (예시)', font=('Arial', 12))],
    [sg.Listbox(values=[
        '1 USD = 1340.50 KRW',
        '1 EUR = 1450.75 KRW',
        '1 JPY = 9.55 KRW',
        '1 CNY = 185.30 KRW',
    ], size=(35, 5), key='-RATES-', font=('Arial', 11))]
]
window = sg.Window('환율 계산기', layout)
import requests
from bs4 import BeautifulSoup as bs

def web_get(url,encoding=""):
    response = requests.get(url)
    if encoding:  # encoding 인자가 주어졌다면 강제로 설정
        response.encoding = encoding    
    html_text = response.text
    return html_text # 함수끝

def find_text(html_text, selector):
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

def fetch_exchange_rates():
    url = "https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=환율"
    html = web_get(url)
    currency_values = find_text_list(html, ".csp .spt_con>strong, .csd .spt_con>strong")
    currency_names = find_text_list(html, ".csp dt em, .csd dt em")

    rates = {}
    for name, value in zip(currency_names, currency_values):
        try:
            code = name.strip()
            rate = float(value.replace(",", ""))
            rates[code] = rate
        except:
            continue
    return rates


# html = web_get("https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&ssc=tab.nx.all&query=%ED%99%98%EC%9C%A8&oquery=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&tqi=juIgLdqosesssOmMU%2FVssssstdR-073184&acq=%ED%99%98%EC%9C%A8&acr=1&qdt=0&ackey=qw01fidy")
# currency_values = find_text_list(html, ".excr_box .recite")
# print(currency_values)

# 이벤트 루프 (화면만 표시)
# 윈도우 이벤트 루프 내부
rate_history = []  # 리스트박스에 추가할 기록 저장용

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '계산하기':
        amount_str = values['-AMOUNT-']
        currency_code = values['-CURRENCY-']
        
        if not amount_str.isdigit():
            window['-RESULT-'].update("금액을 숫자로 입력하세요.")
            continue
        
        amount = float(amount_str)
        rates = fetch_exchange_rates()
        
        if currency_code in rates:
            rate = rates[currency_code]
            result = amount * rate
            result_text = f"{int(amount)} {currency_code} = {int(result):,} KRW"
            window['-RESULT-'].update(result_text)

            # 결과 리스트에 누적 추가
            rate_history.append(result_text)
            window['-RATES-'].update(rate_history)
        else:
            window['-RESULT-'].update("환율 정보를 가져올 수 없습니다.")



window.close()
