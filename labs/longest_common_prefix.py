import sys
from itertools import zip_longest
from typing import List


class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        prefix = []

        for i in zip_longest(*strings):
            if len(set(i)) == 1:
                el = sorted(i, key=len).pop(0)
                prefix.append(el)
            else:
                break

        return ''.join(prefix)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
    sys.exit()
