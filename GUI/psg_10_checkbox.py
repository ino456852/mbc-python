import PySimpleGUI as sg

sg.theme('DarkBlue3')

layout = [  [sg.Checkbox("이메일 수신 동의", default=True, key='-AGREE_EMAIL-')],
            [sg.Checkbox("푸시 알림 받기", key='-AGREE_PUSH-', enable_events=True)], # 상태 변경 시 이벤트 발생
            [sg.Text("", size=(30,1), key='-PUSH_STATUS-')], # 알림 상태 표시용
            [sg.Button("확인"), sg.Button("취소")]
        ]

window = sg.Window("Checkbox 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "취소":
        break

    if event == '-AGREE_PUSH-': # 푸시 알림 체크박스 상태 변경 이벤트
        if values['-AGREE_PUSH-']:
            window['-PUSH_STATUS-'].update("푸시 알림이 켜졌습니다.")
        else:
            window['-PUSH_STATUS-'].update("푸시 알림이 꺼졌습니다.")

    if event == "확인":
        agree_email = values['-AGREE_EMAIL-']
        agree_push = values['-AGREE_PUSH-'] # 이벤트 없이도 현재 값 확인 가능
        print(f"이메일 수신 동의: {agree_email}")
        print(f"푸시 알림 받기: {agree_push}")
        sg.popup(f"이메일 동의: {agree_email}\n푸시 알림: {agree_push}")

window.close()
