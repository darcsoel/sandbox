file = open('urls.txt', 'r')
number = 1
for line in file.readlines():
    try:
        print(line)
    except Exception:
        print('error')

    number += 1
