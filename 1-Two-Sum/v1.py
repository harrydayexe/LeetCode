from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]