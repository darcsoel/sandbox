import collections

some_collection = {'first': 1, 'second': 10}

counter = collections.Counter(some_collection)

print(counter['first'])
print(counter['third'])
