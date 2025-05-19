import PySimpleGUI as sg

layout = [[sg.Input(key='-INPUT-')],
            [sg.Button('Submit')]
        ]

window = sg.Window('Input Example', layout, finalize=True)
window['-INPUT-'].bind("<Return>", "_Enter") # Bind Enter key to event

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit' or event == '-INPUT-_Enter':
        print("Value entered:", values['-INPUT-'])
        break

window.close()