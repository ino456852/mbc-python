# todo_gui.py
import PySimpleGUI as sg
import json
import os

# 파일에서 할일 목록을 불러오는 함수
def load_tasks():
    try:
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except Exception as e:
        sg.popup_error(f'할일 목록을 불러오는 중 오류가 발생했습니다: {e}')
        return []

# 할일 목록을 파일에 저장하는 함수
def save_tasks(tasks):
    try:
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
    except Exception as e:
        sg.popup_error(f'할일 목록을 저장하는 중 오류가 발생했습니다: {e}')

# 리스트박스 업데이트 함수
def update_listbox(window, tasks):
    # 번호 : 내용(상태) 형태로 리스트 생성
    display_list = [f"{i+1} : {t['content']} ({t['status']})" for i, t in enumerate(tasks)]
    window['-LISTBOX-'].update(display_list)

# 입력 필드 초기화 함수
def clear_inputs(window):
    window['-CONTENT-'].update('')
    window['-STATUS-'].update('미완료')
    window['-TASK-ID-'].update('-1')  # 새 할일 등록 모드로 설정

def main():
    # 할일 목록 불러오기
    tasks = load_tasks()
    
    # 상단 패널 - 할일 입력 영역
    input_section = [
        [sg.Text('할일 내용:', size=(10, 1)), sg.InputText(key='-CONTENT-', size=(30, 1), expand_x=True),
         sg.Text('상태:', size=(5, 1)), sg.Combo(['미완료', '진행중', '완료'], default_value='미완료', key='-STATUS-', size=(10, 1)),
         sg.Button('추가', key='-ADD-'), sg.Button('수정', key='-UPDATE-'), sg.Button('취소', key='-CANCEL-')]
    ]
    
    # 하단 패널 - 할일 목록 리스트박스
    list_section = [
        [sg.Listbox(
            values=[f"{i+1} : {t.get('content', '')} ({t.get('status', '미완료')})" for i, t in enumerate(tasks)],
            size=(60, 15),
            key='-LISTBOX-',
            enable_events=True,
            expand_x=True,
            expand_y=True
        )],
        [sg.Button('삭제', key='-DELETE-'), sg.Button('종료', key='-EXIT-')]
    ]
    
    # 전체 레이아웃
    layout = [
        [sg.Text('할일 관리', font=('Helvetica', 16), justification='center', expand_x=True)],
        [sg.Column(input_section, expand_x=True)],
        [sg.HSeparator()],
        [sg.Column(list_section, expand_x=True, expand_y=True)],
        [sg.InputText('', size=(0, 1), visible=False, key='-TASK-ID-')]  # 숨겨진 할일 ID 필드
    ]
    
    window = sg.Window('할일 관리 프로그램', layout, resizable=True, finalize=True)
    window['-TASK-ID-'].update('-1')  # 처음에는 -1(새 할일) 설정
    
    # 이벤트 루프
    while True:
        event, values = window.read()
        
        
        
        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break
        # 추가 버튼 클릭
        if event == "-ADD-":
            content = values["-CONTENT-"] # 할일 내용
            status = values["-STATUS-"] # 상태
            new_task = {
                "content": content,
                "status": status
            }
            tasks.append(new_task) #새 할일 추가
            save_tasks(tasks) # 할 일 저장
            update_listbox(window, tasks) # 갱신
            clear_inputs(window) # 입력값 초기화
            # 할일 목록을 리스트 박스에 갱신(추가,수정,삭제)
        # 리스트 박스 이벤트 처리(할일 목록 클릭)
        if event =='-LISTBOX-':
            sel_txt = values['-LISTBOX-'][0]
            sel_no = int(sel_txt.split(" : ")[0])-1
            sel_task = tasks[sel_no]
            
            window["-CONTENT-"].update(sel_task["content"])
            window["-STATUS-"].update(sel_task["status"])
            window["-TASK-ID-"].update(sel_no)
        # 수정
        if event == "-UPDATE-":
            sel_no = int(values['-TASK-ID-'])
            content = values["-CONTENT-"]
            tasks[sel_no]["content"] = content
            tasks[sel_no]["status"] = values["-STATUS-"]
            save_tasks(tasks)
            update_listbox(window,tasks)
            clear_inputs(window)
        
        # 삭제
        if event == "-DELETE-":    
            sel_txt = values["-LISTBOX-"][0]
            sel_no = int(sel_txt.split(" : ")[0]) - 1
            del tasks[sel_no]
            save_tasks(tasks)
            update_listbox(window, tasks)
            clear_inputs(window)

    
    window.close()

if __name__ == '__main__':
    sg.theme('LightBlue')  # 테마 설정
    main()