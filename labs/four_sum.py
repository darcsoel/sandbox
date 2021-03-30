from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def k_sum(nums, target, count_of_elements):
            nums.sort()

            if not nums:
                return []

            if count_of_elements == 2:
                return two_sum(nums, target)

            result = []

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for _, values in enumerate(k_sum(nums[i + 1:],
                                                     target - nums[i],
                                                     count_of_elements - 1)):
                        result.append([nums[i]] + values)

            return result

        def two_sum(nums, target):
            result = []
            n_count = len(nums) - 1
            left, right = 0, n_count

            while left < right:
                sum_ = nums[left] + nums[right]

                if sum_ < target or (left > 0 and
                                     nums[left] == nums[left - 1]):
                    left += 1
                elif sum_ > target or (right < n_count and
                                       nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

            return result

        nums.sort()
        return k_sum(nums, target, 4)
