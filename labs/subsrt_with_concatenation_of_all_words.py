import itertools
from typing import List


class BruteForceSolution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        words_combinations = itertools.permutations(words)
        words_combinations = set([''.join(words) for
                                  words in words_combinations])
        result = []

        for word in words_combinations:
            start = 0
            while True:
                try:
                    start = s.index(word, start)
                    result.append(start)
                    start += 1
                except ValueError:
                    break

        return result


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        # words_indexes = {}
        #
        # for word in words:
        #     i = 0
        #     while True:
        #         try:
        #             i = s.index(s, i)
        #             words_indexes[i] = word
        #             i += 1
        #         except ValueError:
        #             continue

        result = []

        return result
