import PySimpleGUI as sg
import random

# 난수 설정
com_num = random.randint(1, 100)

sg.theme('LightBlue')

layout = [  
    [sg.Text("1~100 사이 숫자를 맞춰 보세요")],         
    [sg.Text("1~100 사이 숫자:")],
    [sg.Slider(range=(1, 100), default_value=50, orientation='h', size=(30, 15), key='-USER_NUM-', enable_events=True)],
    [sg.Text("현재 번호:"), sg.Text("50", key='-VOL_DISPLAY-')],
    [sg.Button("정답확인")], 
    [sg.Multiline(size=(40, 7), key='-HISTORY-', disabled=True)]
]

window = sg.Window("숫자맞추기 게임", layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # 슬라이더를 움직일 때마다 현재 번호 텍스트에 반영
    if event == '-USER_NUM-':
        user_num = int(values['-USER_NUM-'])
        window['-VOL_DISPLAY-'].update(str(user_num))

    # 정답 확인 시
    if event == "정답확인":
        user_num = int(values["-USER_NUM-"])
        result = f"{user_num} : "

        if com_num == user_num:
            result += "정답입니다!"
            window["-HISTORY-"].update(disabled=False)
            window["-HISTORY-"].print(result)
            ans = sg.popup_yes_no("정답입니다! 다시 하시겠습니까?")
            if ans == "Yes":
                com_num = random.randint(1, 100)
                window["-HISTORY-"].print("새로운 게임 시작!\n")
            else:
                break
        elif com_num > user_num:
            result += "높여주세요"
            sg.popup_error("높여주세요")
            window["-HISTORY-"].print(result)
        else:
            result += "낮춰주세요"
            sg.popup_error("낮춰주세요")
            window["-HISTORY-"].print(result)

window.close()
