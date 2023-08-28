from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        lower, upper = 0, len(nums)
        found = False
        while not found:
            mid = (upper + lower) // 2
            if target < nums[mid]:
                upper = mid - 1
            elif target > nums[mid]:
                lower = mid + 1
            else:
                return mid
