import PySimpleGUI as sg

sg.theme('GreenTan')

layout = [  [sg.Text("선호하는 운영체제는?")],
            [sg.Radio("Windows", group_id="os", key='-WIN-', default=True),
             sg.Radio("macOS", group_id="os", key='-MAC-'),
             sg.Radio("Linux", group_id="os", key='-LINUX-')],
            [sg.Text("결제 수단 선택:")],
            [sg.Radio("신용카드", group_id="payment", key='-CARD-', enable_events=True)],
            [sg.Radio("계좌이체", group_id="payment", key='-TRANSFER-', enable_events=True)],
            [sg.Radio("휴대폰 결제", group_id="payment", key='-MOBILE-', enable_events=True)],
            [sg.Text("", size=(30,1), key='-PAY_INFO-')],
            [sg.Button("제출")]
         ]

window = sg.Window("Radio 버튼 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # 결제 수단 라디오 버튼 이벤트 처리
    if event in ('-CARD-', '-TRANSFER-', '-MOBILE-'):
        if values['-CARD-']:
            window['-PAY_INFO-'].update("신용카드가 선택되었습니다.")
        elif values['-TRANSFER-']:
            window['-PAY_INFO-'].update("계좌이체가 선택되었습니다.")
        elif values['-MOBILE-']:
            window['-PAY_INFO-'].update("휴대폰 결제가 선택되었습니다.")


    if event == "제출":
        selected_os = ""
        if values['-WIN-']: selected_os = "Windows"
        elif values['-MAC-']: selected_os = "macOS"
        elif values['-LINUX-']: selected_os = "Linux"

        selected_payment = ""
        if values['-CARD-']: selected_payment = "신용카드"
        elif values['-TRANSFER-']: selected_payment = "계좌이체"
        elif values['-MOBILE-']: selected_payment = "휴대폰 결제"

        print(f"선호 OS: {selected_os}")
        print(f"결제 수단: {selected_payment}")
        sg.popup(f"선택하신 OS: {selected_os}\n선택하신 결제수단: {selected_payment}")

window.close()
