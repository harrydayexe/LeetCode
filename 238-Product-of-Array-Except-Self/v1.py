from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        forward_product_run = [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                forward_product_run[i] = num
            else:
                forward_product_run[i] = num * forward_product_run[i-1]

        backward_product_run = [0] * len(nums)

        for i, num in enumerate(reversed(nums)):
            if i == 0:
                backward_product_run[i] = num
            else:
                backward_product_run[i] = num * backward_product_run[i - 1]

        backward_product_run.reverse()

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(backward_product_run[i+1])
            elif i + 1 == len(nums):
                output.append(forward_product_run[i-1])
            else:
                output.append(forward_product_run[i-1] * backward_product_run[i+1])

        return output
