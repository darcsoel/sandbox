import bisect
import sys

if __name__ == '__main__':
    data = [x for x in range(5)] + [x for x in range(6, 9)]

    print(data)

    print(bisect.bisect(data, 5))
    print(bisect.bisect(data, 7))
    print(bisect.bisect(data, 12))

    print(data)

    sys.exit()
