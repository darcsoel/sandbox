import string
import sys


class Solution:
    def myAtoi(self, number: str) -> int:
        acceptable = list(string.digits) + ['+', '-']

        # remove leading spaces
        while True:
            space = number.find(' ')
            if space == 0:
                number = number[1:]
            elif space > 0:
                number = number[:space]
            else:
                break

        # remove all after second `-` or `+` symbol
        sign = False
        for index, symbol in enumerate(number):
            if symbol in ('-', '+'):
                if sign:
                    number = number[:index]
                    break
                sign = True

        for index, symbol in enumerate(number):
            if symbol not in acceptable:
                number = number[:index]
                break

        for index, symbol in enumerate(number):
            if symbol in ('-', '+'):
                if index > 0 and number[index - 1].isdigit():
                    number = number[:index]
                    break

        sign = False
        minus = False

        if not number:
            return 0

        if not number.isnumeric():
            clean = []
            for n in number:
                if n in ('-', '+'):
                    if n == '-':
                        minus = True
                    if sign:
                        break
                    sign = True
                    continue
                if n.isnumeric():
                    clean.append(n)
                else:
                    if sign:
                        break
                    else:
                        break
            number = clean

        result = 0
        zero_code = ord('0')

        for index, symbol in enumerate(number, 1):
            result += (ord(symbol) - zero_code) * 10 ** (len(number) - index)

        result = result if not minus else -result

        max_positive = (2 ** 31) - 1
        max_negative = -2 ** 31

        if result > max_positive:
            return max_positive
        if result < max_negative:
            return max_negative
        return result


if __name__ == '__main__':
    numbers = {'  10 ': 10,
               '-14': -14,
               '2 dfdsf': 2,
               'sdf 4': 0,
               '3.1415': 3,
               '+1': 1,
               "  -0012a42": -12,
               "   +0 123": 0,
               "-13+8": -13,
               '.1': 0,
               '-+12': 0,
               '123-': 123,
               ' ++1': 0,
               "21474836++": 21474836,
               "     +004500": 4500,
               "23a8f": 23,
               "+-12": 0,
               "  +b12102370352": 0,
               "00000-42a1234": 0
               }

    answers = []
    # numbers = {"     +004500": 4500,}
    for number_entity, answer in numbers.items():
        check = Solution().myAtoi(number_entity)
        correct = check == answer
        print(number_entity, correct)
        answers.append(correct)

    print("\n")
    print('all correct = ', all(answers))
    sys.exit()
