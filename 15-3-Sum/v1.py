from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [[x, y, z] for x, y, z in output]
