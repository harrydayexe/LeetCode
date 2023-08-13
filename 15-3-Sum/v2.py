from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == 0 - nums[i]:
                    output.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                elif nums[l] + nums[r] < 0 - nums[i]:
                    l += 1
                else:
                    r -= 1

        return [[x, y, z] for x, y, z in output]
