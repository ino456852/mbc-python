import PySimpleGUI as sg

# 1. 테마 설정 (선택 사항이지만, 보기 좋은 UI를 위해 권장)
sg.theme('DarkAmber') # 다양한 테마를 사용해 보세요: 'DarkAmber', 'LightGreen', 'BluePurple' 등

# 2. 레이아웃(Layout) 정의: 창에 표시될 요소들을 리스트의 리스트 형태로 정의합니다.
#    각 내부 리스트는 한 줄(row)을 의미합니다.
layout = [  
            [sg.Text("GUI연습!")],  # 첫 번째 줄: 텍스트 요소
            [sg.Button("확인")], # 두 번째 줄: 버튼 요소
            [sg.Button("취소")] # 두 번째 줄: 버튼 요소
        ]   

# 3. 윈도우(Window) 생성: 제목과 레이아웃을 지정하여 창을 만듭니다.
window = sg.Window("My First App", layout, size=( 300, 100))

# 4. 이벤트 루프(Event Loop): 사용자의 액션(이벤트)을 감지하고 처리합니다.
while True:
    event, values = window.read()  # 창으로부터 이벤트와 입력 값들을 읽어옵니다.

    # 사용자가 창을 닫거나 "OK" 버튼을 누르면 루프를 종료합니다.
    # if event == sg.WIN_CLOSED or event == "확인" or event == "취소":
    if event in (sg.WIN_CLOSED, "확인", "취소"):
        break

# 5. 윈도우 닫기: 프로그램 종료 전에 창을 닫습니다.
window.close()

print("프로그램이 종료되었습니다.")
