from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        found = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if found.get(difference, -1) != -1:
                return [found.get(difference, -1), i]
            else:
                found[nums[i]] = i
