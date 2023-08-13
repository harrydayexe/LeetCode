from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == 0 - nums[i]:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] < 0 - nums[i]:
                    l += 1
                else:
                    r -= 1

        return output
