import PySimpleGUI as sg
import cr_10_오픈웨더 as we
sg.theme('LightBlue')

layout = [
    # 상단: 도시 입력 필드 + 버튼
    [sg.Text('도시 이름:'), sg.Input(key='-CITY_INPUT-', size=(20, 1)), sg.Button('날씨 가져오기')],

    # 현재 날씨 정보 영역
    [sg.Text('현재 날씨: ', size=(30,1), key='-WEATHER-', font=('Arial', 14))],
    [sg.Text('현재 온도: ', size=(30,1), key='-TEMP-', font=('Arial', 14))],
    [sg.Text('현재 습도: ', size=(30,1), key='-HUMIDITY-', font=('Arial', 14))],

    # 날씨 예보 리스트
    [sg.Text('5일치 날씨 예보', font=('Arial', 14))],
    [sg.Listbox(values=[
        '예보를 불러오려면 도시 이름을 입력하세요.'
    ],
    size=(35, 5), key='-FORECAST-', font=('Arial', 12))]
]

# 창 생성
window = sg.Window('도시 날씨 알림', layout, finalize=True)

# 이벤트 루프 (데이터 연동 없이 화면만 구성)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == '날씨 가져오기':
        city = values['-CITY_INPUT-']
        w = we.get_weather(city)
        # 여기서 API 호출 및 업데이트 로직 추가 가능
        # 아래는 임시 표시용 예시
        window['-WEATHER-'].update('현재 날씨: %s %s ' % (w['weather'],[city]) )
        window['-TEMP-'].update('현재 온도: %s℃' % (w['temp']))
        window['-HUMIDITY-'].update('현재 습도: %s' % (w['feels_like']))
        window['-FORECAST-'].update([
            '5/22 - 맑음 - 23°C/14°C',
            '5/23 - 구름많음 - 21°C/15°C',
            '5/24 - 비 - 19°C/13°C',
            '5/25 - 맑음 - 22°C/12°C',
            '5/26 - 흐림 - 20°C/14°C'
        ])

window.close()
