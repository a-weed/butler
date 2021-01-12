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

window = sg.Window('Airac', layout)

def print_hi(hi_name):
    print(f'Hi, {hi_name}')


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
    print("Today is " + weekday.get(day, "Invalid Choice of Weekday"))
    return day


# parser needs to read file first, then add option to add tasks in terminal
def parseToday(day):
    df = pd.read_csv('tasks.txt')
    tasks = df.values
    length = (tasks.size / 3)
    i = 0
    while(i<length):
        if tasks[i,0] == day:
            print(tasks[i,2])
        i += 1


window.close()

if __name__ == '__main__':
    print(";)")
    name = "Alex"
    print_hi(name)
    done = False
    while not done:
        print("What would you like to do?\n" +
              "0: Arithmetic // 1: Financials // 2: ToDay")
        choice = int(input())
        #print("You chose " + get_action_field(choice))
        if choice == 0:
            arithmetic()
        elif choice == 1:
            fin_viz()
        elif choice == 2:
            day = today()
            parseToday(day)
        else:
            print("Invalid Choice")
            done = True
    print('Byeeee')
