arr = [1, 2, 3, 4]
for z, i in enumerate(arr):
    i = 1
    arr[z] = 2

print(arr)

arr = iter([1, 2, 3, 4])
print(arr)

for i in arr:
    print(i)

print(arr)

for i in arr:
    print(i)
