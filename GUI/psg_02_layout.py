import PySimpleGUI as sg

sg.theme('LightBlue')

layout = [  [sg.Text("이름:"), sg.InputText()],         # 첫 번째 줄: 텍스트와 입력 필드
            [sg.Text("나이:"), sg.InputText(size=(5,1))], # 두 번째 줄: 텍스트와 크기가 지정된 입력 필드
            [sg.Button("확인"), sg.Button("취소")]      # 세 번째 줄: 버튼 두 개
         ]

window = sg.Window("정보 입력", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "취소":
        break
    if event == "확인":
        # 여기서 values 값을 사용하게 됩니다 (2.4절에서 자세히 설명)
        print(f"입력된 값: {values}")

window.close()
