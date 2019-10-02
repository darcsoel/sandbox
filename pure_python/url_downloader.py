from urllib.parse import urlparse
import urllib.request

file = open('urls.txt', 'r')
number = 0

for line in file.readlines():
    try:
        print(line)
        with urllib.request.urlopen(line) as response:
            html = response.read()
            print(html)
        number += 1
    except IOError as error:
        print(error)


print(number)
