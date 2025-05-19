import PySimpleGUI as sg

sg.theme('Reddit')

# 이미지 버튼을 위해 실제 이미지 파일 (예: 'icon.png')이 필요합니다.
# 없다면 image_filename 부분은 주석 처리하거나 제외하세요.
layout = [  [sg.Button("기본 버튼"), sg.Button("색상 버튼", button_color=('white', 'green'))],
            [sg.Button("큰 버튼", size=(15,2)), sg.Button("비활성 버튼", disabled=True)],
            # [sg.Button(image_filename='icon.png', key='-IMG_BTN-'), sg.Text("이미지 버튼")], # 이미지 파일 필요
            [sg.Ok(), sg.Cancel(), sg.Button("커스텀 키 버튼", key='-CUSTOM-')]
         ]

window = sg.Window("Button 엘리먼트 예제", layout)

while True:
    event, values = window.read()
    print(f"Event: {event}")
    if event == sg.WIN_CLOSED or event == "Cancel" or event == "OK": # Ok()는 "OK" 이벤트 반환
        break
    if event == "-CUSTOM-":
        print("커스텀 키 버튼이 눌렸습니다!")
    # elif event == '-IMG_BTN-':
    #     print("이미지 버튼이 눌렸습니다!")

window.close()
