class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        for index, sym in enumerate(haystack):
            try:
                if haystack[index:index + len(needle)] == needle:
                    return index
            except IndexError:
                return -1
        return -1
