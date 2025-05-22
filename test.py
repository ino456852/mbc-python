import PySimpleGUI as sg
import cr_10_오픈웨더 as we  # get_weather(), get_forecast()

sg.theme('LightBlue')

layout = [
    [sg.Text('도시 이름:'), sg.Input(key='-CITY_INPUT-', size=(20, 1)), sg.Button('날씨 가져오기')],
    [sg.Text('현재 날씨: ', size=(30,1), key='-WEATHER-', font=('Arial', 14))],
    [sg.Text('현재 온도: ', size=(30,1), key='-TEMP-', font=('Arial', 14))],
    [sg.Text('현재 체감온도: ', size=(30,1), key='-HUMIDITY-', font=('Arial', 14))],
    [sg.Text('5일치 날씨 예보', font=('Arial', 14))],
    [sg.Listbox(values=['예보를 불러오려면 도시 이름을 입력하세요.'],
                size=(60, 7), key='-FORECAST-', font=('Arial', 12))]
]

window = sg.Window('도시 날씨 알림', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == '날씨 가져오기':
        city = values['-CITY_INPUT-'].strip()
        if not city:
            sg.popup("도시 이름을 입력하세요.")
            continue

        try:
            w = we.get_weather(city)
            forecast = we.get_forecast(city)

            # 현재 날씨 업데이트
            window['-WEATHER-'].update(f"현재 날씨: {w['weather']} ({city})")
            window['-TEMP-'].update(f"현재 온도: {w['temp']}℃")
            window['-HUMIDITY-'].update(f"체감 온도: {w['feels_like']}℃")

            # 5일 예보 표시 (하루 1개씩 요약 예보를 원한다면, 12:00:00 기준으로 필터링 가능)
            window['-FORECAST-'].update(forecast[:5])  # 앞에서 5개만

        except Exception as e:
            sg.popup("날씨 정보를 가져오는 데 실패했습니다.", str(e))

window.close()
