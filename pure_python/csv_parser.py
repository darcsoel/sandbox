import csv


result = []

with open('posts.csv') as file:
    csvf = csv.reader(file)
    for row in csvf:
        result.append(row)

print(result)
headers = result[0]
result = result[1:]

print(headers)
print(result)

