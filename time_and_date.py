import time

localtime = time.localtime(time.time())

print(localtime.tm_year)
print(localtime.tm_yday)
print(localtime.tm_zone)

x = [i for i in range(10)]
print(x)
