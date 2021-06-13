from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i = 0

        while i < len(nums):
            cur = nums[i]

            if cur == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
