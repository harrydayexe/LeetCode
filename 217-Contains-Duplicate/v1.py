from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False
