import PySimpleGUI as sg

sg.theme('LightBrown_DarkBrown_LightBrown')

layout = [  [sg.Text("이름:"), sg.InputText(key='-NAME-')],
            [sg.Text("나이:"), sg.Input(size=(5,1), key='-AGE-')],
            [sg.Text("비밀번호:"), sg.Input(password_char='*', key='-PASSWORD-')],
            [sg.Text("설명 (읽기전용):"), sg.Input("수정 불가", readonly=True, size=(20,1))],
            [sg.Button("제출"), sg.Button("취소")]
         ]

window = sg.Window("InputText 엘리먼트 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "취소":
        break
    if event == "제출":
        name = values['-NAME-']
        age = values['-AGE-']
        password = values['-PASSWORD-']
        print(f"이름: {name}, 나이: {age}, 비밀번호: {password}")
        if not age.isdigit(): # 간단한 유효성 검사
            sg.popup_error("나이는 숫자로 입력해주세요.")

window.close()
