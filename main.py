import pandas as pd
import numpy as np
import datetime
import PySimpleGUI as sg

#Mr. Dalliard
sg.theme('DarkAmber')

#Fix formatting
layout = [[sg.Text(';)')],
            [sg.Text('What must be done?')],
            [sg.Button('A'), sg.Text('Arithmetic')],
            [sg.Button('S'), sg.Text('Stonks')],
            [sg.Button('B'), sg.Text('Butler')],
            [sg.Button('Exit')]]

layoutButler = [[sg.Text('Press Load                                       ', key='-text-')],
                [sg.Text("Tasks")],
                [sg.Text('None :)                                                       ', key='-tasks-')],
                [sg.Button('Load'), sg.Button('Exit')]]

window = sg.Window('Airac', layout)
butlerWin = sg.Window('Butler', layoutButler, resizable=True)


def get_action_field(argument):
    switcher = {
        0: "Arithmetic",
        1: "FinViz",
        2: "ToDay"
    }
    return switcher.get(argument, "Invalid Choice")


def arithmetic():
    print(7 * 6)
    return


def fin_viz():
    print("$$$")
    return


def today():
    day = datetime.datetime.today().weekday()
    weekday = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    weekday = weekday.get(day, "Invalid Choice of Weekday")
    return day, weekday



def parseToday(day):
    df = pd.read_csv('tasks.txt')
    tasks = df.values
    tasklist = ''
    length = (tasks.size / 4)
    i = 0
    while(i<length):
        # if tasks[i,0] == day or tasks[i,0] == 8
        if (str(day) in str(tasks[i,0])) or ('8' in str(tasks[i,0])):
            tasklist += tasks[i,2]
            tasklist += "\n"
        i += 1
    return tasklist

# todo only need to parse today once, can manually re-do through Load button
# todo addTask()
# todo schedule order (times in array)
def butlerUI():
    global inButler
    day, weekday = today()
    tasklist = parseToday(day)
    event, values = butlerWin.Read(timeout=500, timeout_key="__BUTLER_TIMEOUT__")
    print(f"You clicked {event}")
    butlerWin['-text-'].set_size((None, 4))
    butlerWin['-tasks-'].set_size((None,15))
    butlerWin['-text-'].update("Today is: " + weekday )
    butlerWin['-tasks-'].update(tasklist)
    if event == sg.WIN_CLOSED or event == 'Exit':
        inButler = False
        butlerWin.close()

inButler = False
while True:
    event, values = window.Read(timeout=3000, timeout_key="__TIMEOUT__")
    print(f"You clicked {event}")
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'B':
        inButler= True
        butlerUI()
    if event == 'S':
        fin_viz()
    if event == 'A':
        arithmetic()
    if inButler == True:
        butlerUI()




butlerWin.close()
window.close()
print('Byeeee')

# while True:
#     event, values = window1.Read(timeout=500)
#     # do something with the info
#     event, values = window2.ReadNonBlocking()
#     # do something with these values too
