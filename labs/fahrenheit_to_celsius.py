"""Standard task with temperature system translate"""

import sys


def c_style():
    start = 0
    finish = 300
    step = 20
    curr_fahrenheit = start

    while curr_fahrenheit < finish:
        celsius = 5 * (curr_fahrenheit - 32) / 9
        print(curr_fahrenheit, celsius)
        curr_fahrenheit += step


def python_style():
    for fahrenheit in range(0, 400, 10):
        celsius = 5 * (fahrenheit - 32) / 9
        print("Fahrenheit\t", fahrenheit, "\tCelsius\t", celsius)


if __name__ == '__main__':
    python_style()
    sys.exit()
