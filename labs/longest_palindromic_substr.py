import sys


# brute force
def longest_palindrome(long_string: str) -> str:
    results = []

    for char_index, _ in enumerate(long_string):
        result = []
        for index in range(char_index, len(long_string)):
            result.append(long_string[index])

            if result == result[::-1]:
                results.append(''.join(result))

    return max(results, key=len)


# Manacher's algorithm
class Solution:
    def longestPalindrome(self, long_string: str) -> str:
        longest_check = [' ' for _ in range(len(long_string) * 2 + 1)]

        for index, char in enumerate(long_string):
            longest_check[index * 2 + 1] = char

        radius_array = [0 for _ in longest_check]
        current_index = right_border = center = 0
        pal_max_len = 1

        for index in range(len(longest_check) - 1):
            mirror = 2 * center - index
            radius_array[index] = min(radius_array[mirror],
                                      right_border - index) \
                if right_border > index else 0

            while index > radius_array[index] and \
                    (index + radius_array[index] + 1) < len(longest_check) \
                    and longest_check[index - radius_array[index] - 1] \
                    == longest_check[index + radius_array[index] + 1]:
                radius_array[index] += 1

            if radius_array[index] + index > right_border:
                center = index
                right_border = index + radius_array[index]

            if pal_max_len < radius_array[index]:
                pal_max_len = radius_array[index]
                current_index = index

        start_point = round((current_index - pal_max_len) / 2)
        return long_string[start_point: start_point + pal_max_len]


if __name__ == '__main__':
    palindromic_strings = ['babad', 'cbbd', 'a', 'ac', 'aaaa', 'bb', 'abcba']

    for s in palindromic_strings:
        print(s, ' is palindromic ', Solution().longestPalindrome(s))

    sys.exit()
