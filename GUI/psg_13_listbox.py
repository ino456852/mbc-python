import PySimpleGUI as sg

sg.theme('LightGrey1')

options = ['옵션 A', '옵션 B', '옵션 C', '옵션 D', '옵션 E', '옵션 F']

layout = [  [sg.Text("단일 선택 리스트박스:")],
            [sg.Listbox(options, size=(20, 4), key='-SINGLE_LB-', enable_events=True)],
            [sg.Text("다중 선택 리스트박스 (Ctrl/Shift 키 사용):")],
            [sg.Listbox(options, size=(20, 4), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-MULTI_LB-', default_values=[options[1], options[3]])],
            [sg.Text("선택된 항목:", size=(15,1)), sg.Text("", size=(30,2), key='-STATUS-')],
            [sg.Button("확인")]
         ]

window = sg.Window("Listbox 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-SINGLE_LB-': # 단일 선택 리스트박스 이벤트
        if values['-SINGLE_LB-']: # 선택된 항목이 있을 경우 (리스트가 비어있지 않으면)
            window['-STATUS-'].update(f"단일: {values['-SINGLE_LB-'][0]}")
        else:
            window['-STATUS-'].update("단일: 선택 없음")


    if event == "확인":
        single_selected = values['-SINGLE_LB-']
        multi_selected = values['-MULTI_LB-']

        print(f"단일 선택: {single_selected}")
        print(f"다중 선택: {multi_selected}")
        sg.popup(f"단일: {single_selected}\n다중: {multi_selected}")
        # 선택된 항목이 없을 경우 빈 리스트 [] 가 반환됨

window.close()
