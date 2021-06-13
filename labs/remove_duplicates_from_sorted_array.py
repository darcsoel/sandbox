from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1

        while i < len(nums):
            prev = nums[i - 1]
            cur = nums[i]

            if cur == prev:
                nums.pop(i - 1)
            else:
                i += 1

        return len(nums)
