import PySimpleGUI as sg
import time # 로그 출력 예제를 위해

sg.theme('Material1')

log_output_key = '-LOG-'

layout = [  [sg.Text("메모를 입력하세요:")],
            [sg.Multiline(size=(40, 5), key='-MEMO-', default_text="여기에 여러 줄 입력 가능...\n두 번째 줄입니다.")],
            [sg.Button("저장"), sg.Button("로그 시작")],
            [sg.Text("프로그램 로그:")],
            [sg.Multiline(size=(40, 8), key=log_output_key, autoscroll=True, disabled=True)]
         ]

window = sg.Window("Multiline 엘리먼트 예제", layout)

log_counter = 0

while True:
    event, values = window.read(timeout=1000) # 1초마다 timeout 이벤트 발생 (로그 예제용)

    if event == sg.WIN_CLOSED:
        break
    if event == "저장":
        memo_text = values['-MEMO-']
        print("--- 저장된 메모 ---")
        print(memo_text)
        sg.popup("메모가 콘솔에 저장(출력)되었습니다.")
    if event == "로그 시작":
        window[log_output_key].update(disabled=False) # 로그창 활성화
        window["로그 시작"].update(disabled=True) # 버튼 비활성화
    elif event == sg.TIMEOUT_KEY and window["로그 시작"].Disabled: # '로그 시작' 버튼이 눌린 후에만
        log_counter += 1
        # Multiline에 텍스트 추가하는 방법 1: print 메소드 사용
        window[log_output_key].print(f"{time.strftime('%H:%M:%S')} - 로그 메시지 {log_counter}")
        # 방법 2: update 메소드 사용 (기존 내용에 추가하려면 + 연산자나 f-string 필요)
        # current_log = values[log_output_key] # 현재 로그 가져오기 (주의: 매우 긴 로그에는 비효율적일 수 있음)
        # window[log_output_key].update(current_log + f"{time.strftime('%H:%M:%S')} - 로그 메시지 {log_counter}\\n")


window.close()
