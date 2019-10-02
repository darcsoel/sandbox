import os

curr_directory = os.path.dirname((os.path.abspath(__file__)))
print(curr_directory)

print(os.listdir(curr_directory))

line_number = 0
with open('array_numpy.py') as a_file:
    for line in a_file:
        line_number += 1
        print('{} --> {}'.format(line_number, line))
