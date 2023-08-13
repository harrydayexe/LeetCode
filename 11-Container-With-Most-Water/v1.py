from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        area = (len(height) - 1) * min(height[0], height[-1])
        l, r = 0, len(height) - 1
        while l < r:
            new_area = (r - l) * min(height[l], height[r])
            if area < new_area:
                area = new_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
