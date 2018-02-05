import os

curr_directory = os.path.dirname((os.path.abspath(__file__)))
print(curr_directory)

print(os.listdir(curr_directory))
