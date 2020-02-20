import collections

ordered = collections.OrderedDict()

for i in reversed(range(10)):
    ordered.update({str(i): f'some value {i}'})

print(ordered)

ordered.move_to_end('9')

print(ordered)
