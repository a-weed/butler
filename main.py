import pandas as pd
import numpy as np
import datetime
import PySimpleGUI as sg

sg.theme('DarkAmber')

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
    print("Today is " + weekday)
    return day, weekday


# parser needs to read file first, then add option to add tasks in terminal
def parseToday(day):
    df = pd.read_csv('tasks.txt')
    tasks = df.values
    tasklist = ''
    length = (tasks.size / 3)
    i = 0
    while(i<length):
        if tasks[i,0] == day:
            tasklist += tasks[i,2]
            tasklist += "\n"
            print(tasks[i,2])
        i += 1
    return tasklist

def butlerUI():
    while True:
        day, weekday = today()
        tasklist = parseToday(day)

        eventb, valuesb = butlerWin.read()
        butlerWin['-text-'].set_size((None,4))
        butlerWin['-tasks-'].set_size((None,15))
        butlerWin['-text-'].update("Today is: " + weekday )
        butlerWin['-tasks-'].update(tasklist)
        if eventb == 'Load':
            continue
        if eventb == sg.WIN_CLOSED or eventb == 'Exit':
            butlerWin.close()
            break

while True:
    event, values = window.read()
    print("You clicked " + str(event))
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'B':
        butlerUI()




window.close()
print('Byeeee')
