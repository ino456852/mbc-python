from logging import PlaceHolder
import PySimpleGUI as sg
import naver_search_crawling as cr

layout = [
    [sg.Text('사이트 주소:'), sg.Input(key='-URL-', size=(50,1))],
    [sg.Text('선택자 입력:'), sg.Input(key='-SELECTOR-', size=(50,1))],
    [sg.Button('검색', size=(10,1))],
    [sg.Text('결과 목록:')],
    [sg.Listbox(values=[], size=(70, 15), key='-RESULT-', enable_events=True)]
]

window = sg.Window('크롤링 결과 보기', layout)

while True:
    event, values = window.read() 
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "검색":
        url = values["-URL-"]
        selector = values["-SELECTOR-"]
        html = cr.web_get(url,"utf-8")
        text_list = cr.find_text_list(html,selector)
        window['-RESULT-'].Update(text_list)

window.close()