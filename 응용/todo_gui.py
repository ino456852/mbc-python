import PySimpleGUI as sg
import todo_logic

# 버튼 스타일 설정
button_size = (5, 2)
button_font = ('Arial', 16)

# 레이아웃 설계
layout = [
    [sg.Input('', size=(20, 1), key='-DISPLAY-',
              justification='right', font=('Arial', 20), disabled=True)],
    [sg.Button('7', size=button_size, font=button_font), sg.Button('8', size=button_size, font=button_font), sg.Button(
        '9', size=button_size, font=button_font), sg.Button('/', size=button_size, font=button_font)],
    [sg.Button('4', size=button_size, font=button_font), sg.Button('5', size=button_size, font=button_font), sg.Button(
        '6', size=button_size, font=button_font), sg.Button('*', size=button_size, font=button_font)],
    [sg.Button('1', size=button_size, font=button_font), sg.Button('2', size=button_size, font=button_font), sg.Button(
        '3', size=button_size, font=button_font), sg.Button('-', size=button_size, font=button_font)],
    [sg.Button('0', size=button_size, font=button_font), sg.Button('.', size=button_size, font=button_font), sg.Button(
        '=', size=button_size, font=button_font), sg.Button('+', size=button_size, font=button_font)],
    [sg.Button('C', size=(22, 1), font=button_font),
     sg.Button('종료', size=(6, 1), font=button_font)]
]

# 창 생성
window = sg.Window(
    '계산기', layout, element_justification='center')  # 창 내부 가운데 정렬

# 현재 수식 저장용 변수
current_input = ''

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, '종료'):
        break

    # 숫자/연산자 버튼 클릭 시
    if event in '0123456789.+-*/':
        current_input = todo_logic.regist(event, current_input)

    # = 버튼 클릭 시 계산 수행
    elif event == '=':
        current_input = todo_logic.update(current_input)

    # C 버튼 클릭 시 마지막 입력 삭제
    elif event == 'C':
        current_input = todo_logic.delete(current_input)

    # 결과 또는 수식 표시
    window['-DISPLAY-'].update(current_input)


window.close()
