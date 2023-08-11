from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)

        longest_size = 1
        current_size = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                current_size += 1
                longest_size = max(longest_size, current_size)
            else:
                current_size = 1

        return longest_size
