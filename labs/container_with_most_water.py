"""Given n non-negative integers a1, a2, ..., an , where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that the
two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which,
together with the x-axis forms a container, such that the container contains
the most water.

Notice that you may not slant the container.
"""
from typing import List


class Solution:
    def __init__(self):
        self._max_area = 0
        self._start = self._end = 0

    def maxArea(self, height: List[int]) -> int:
        self._end = len(height) - 1

        while self._start < self._end:
            h_min = min(height[self._start], height[self._end])
            max_area = h_min * (self._end - self._start)
            self._max_area = max(max_area, self._max_area)

            if height[self._start] < height[self._end]:
                self._start += 1
            else:
                self._end -= 1

        return self._max_area
