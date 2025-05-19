import PySimpleGUI as sg

sg.theme('DarkTeal_DarkTeal')

layout = [  [sg.Text("볼륨 조절 (0-100, 단위 1):")],
            [sg.Slider(range=(0, 100), default_value=50, orientation='h', size=(20, 15), key='-VOLUME-', enable_events=True)],
            [sg.Text("밝기 조절 (0.0-1.0, 단위 0.1):")],
            [sg.Slider(range=(0.0, 1.0), default_value=0.5, resolution=0.05, orientation='h', size=(20,15), key='-BRIGHTNESS-', tick_interval=0.2)],
            [sg.Text("수직 슬라이더 (1-10):"),
             sg.Slider(range=(1, 10), default_value=3, orientation='v', size=(10,20), key='-V_SLIDER-')],
            [sg.Text("현재 볼륨:"), sg.Text("50", key='-VOL_DISPLAY-')],
            [sg.Button("적용")]
         ]

window = sg.Window("Slider 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-VOLUME-': # 볼륨 슬라이더 값 변경 이벤트
        volume_value = int(values['-VOLUME-']) # 슬라이더 값은 float일 수 있으므로 필요시 int로 변환
        window['-VOL_DISPLAY-'].update(str(volume_value))

    if event == "적용":
        volume = int(values['-VOLUME-'])
        brightness = values['-BRIGHTNESS-'] # float 값
        v_slider_val = int(values['-V_SLIDER-'])

        print(f"볼륨: {volume}, 밝기: {brightness:.2f}, 수직 슬라이더: {v_slider_val}")
        sg.popup(f"볼륨: {volume}\n밝기: {brightness:.2f}\n수직: {v_slider_val}")

window.close()
