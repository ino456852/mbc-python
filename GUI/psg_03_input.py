import PySimpleGUI as sg

sg.theme('DarkGrey_DarkGrey')

layout = [  [sg.Text("사용자 ID:"), sg.InputText(key='-USERID-')],
            [sg.Text("비밀번호:"), sg.InputText(key='-PASSWORD-', password_char='*')],
            [sg.Button("로그인"), sg.Button("취소")] ] # '로그인' 버튼에는 key를 주지 않고 텍스트로 이벤트 처리

window = sg.Window("로그인 창", layout)

while True:
    event, values = window.read()
    print(f"Event: {event}") # 어떤 이벤트가 발생하는지 확인
    print(f"Values: {values}") # values 딕셔너리 내용 확인

    if event in (sg.WIN_CLOSED, "취소"):
        break
    if event == "로그인":
        # values 딕셔너리에서 key를 사용하여 입력값을 가져옵니다.
        user_id = values['-USERID-']
        password = values['-PASSWORD-']

        print(f"입력한 ID: {user_id}")
        print(f"입력한 비밀번호: {password}")

        if user_id == "admin" and password == "1234":
            sg.popup("로그인 성공!")
        else:
            sg.popup_error("ID 또는 비밀번호가 잘못되었습니다.")

window.close()
