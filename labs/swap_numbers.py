import sys


def main():
    numbers = input('Enter whitespace-separate numbers: ')
    first, second = numbers.split(' ')

    if not first and not second:
        raise SystemError('You entered just one number')

    print(f'Reversed => {second}; {first}')
    return


if __name__ == '__main__':
    main()
    sys.exit()
