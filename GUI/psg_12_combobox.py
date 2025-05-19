import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

font_list = ['Arial', 'Courier New', 'Comic Sans MS', 'Helvetica', 'Times New Roman']
size_list = [str(i) for i in range(8, 17, 2)] # 8, 10, 12, 14, 16

layout = [  [sg.Text("글꼴 선택:"), sg.Combo(font_list, default_value=font_list[0], key='-FONT-', readonly=True, enable_events=True)],
            [sg.Text("크기 선택:"), sg.Combo(size_list, default_value=size_list[2], key='-SIZE-', readonly=True, size=(5,1))],
            [sg.Text("선택된 폰트: ", key='-FONT_DISPLAY-'), sg.Text(font_list[0], key='-SELECTED_FONT-')],
            [sg.Button("적용")]
         ]

window = sg.Window("Combo 예제", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-FONT-': # 폰트 콤보박스 변경 이벤트
        selected_font_name = values['-FONT-']
        window['-SELECTED_FONT-'].update(selected_font_name)
        print(f"폰트 변경됨: {selected_font_name}")

    if event == "적용":
        final_font = values['-FONT-']
        final_size = values['-SIZE-']
        print(f"적용된 폰트: {final_font}, 크기: {final_size}")
        sg.popup(f"폰트: {final_font}\n크기: {final_size} 로 설정 (실제 적용은 미구현)")

window.close()
