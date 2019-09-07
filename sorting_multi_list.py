from operator import itemgetter

arr = [
    [1, 'test'],[2, 'dsfsf'],[3, 'awsw']
]

sorted_array = sorted(arr, key=itemgetter(1))

print(sorted_array)
