import PySimpleGUI as sg

sg.theme('SandyBeach')

layout = [  [sg.Text("기본 텍스트입니다.")],
            [sg.Text("크기를 지정한 텍스트 (25글자 너비)", size=(25, 1))],
            [sg.Text("색상과 폰트를 바꾼 텍스트", text_color='blue', font=('Arial', 14))],
            [sg.Text("오른쪽 정렬 텍스트", size=(30,1), justification='right', background_color='lightgrey')],
            [sg.Text("여백을 추가한 텍스트", pad=((100,100),(50,50)), background_color='lightblue')],
            [sg.Text("키를 가진 텍스트", key='-MY_TEXT-')]
         ]

window = sg.Window("Text 엘리먼트 예제", layout)

# 이벤트 루프에서 -MY_TEXT- 를 업데이트 해볼 수도 있습니다. (6장에서 자세히)
# 예: window['-MY_TEXT-'].update("텍스트가 변경되었습니다!")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
