import collections

User = collections.namedtuple('User', ['name', 'age'])

John = User(name='John', age=20)

print(f'Created namedtuple - {John}')
