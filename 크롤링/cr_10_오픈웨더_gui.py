# cr_10_오픈웨더_gui.py
import PySimpleGUI as sg
import cr_10_오픈웨더 as we
import cr_11_geo_coding as geo
# GUI 레이아웃 정의
layout = [
    [sg.Text('도시 이름을 입력하세요:'), sg.Input(key='-CITY-'), sg.Button('날씨 가져오기')],
    [sg.Text('현재 온도:', size=(12,1)), sg.Text('--- ℃', key='-TEMP-')],
    [sg.Text('습도:', size=(12,1)), sg.Text('--- %', key='-HUMID-')],
    [sg.Text('날씨:', size=(12,1)), sg.Text('---', key='-DESC-')],
]

# 창 생성
window = sg.Window('날씨 정보 조회 (화면만)', layout)

# 이벤트 루프 (닫기만 가능)
while True:
    event, values = window.read()
    print(f"Event: {event}") # 어떤 이벤트가 발생하는지 확인
    print(f"Values: {values}") # values 딕셔너리 내용 확인
    if event == "날씨 가져오기":
        city = values['-CITY-']
        w = we.get_weather(city)
        print(w)
        window['-TEMP-'].update(w['temp'])
        window['-HUMID-'].update(w['feels_like'])
        window['-DESC-'].update(w['weather'])
    
    if event == sg.WINDOW_CLOSED:
        break

window.close()