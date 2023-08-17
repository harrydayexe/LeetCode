from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        tallest = max(height)
        output = 0
        for y in range(tallest, -1, -1):
            l_wall_found = False
            potential_add = 0
            for x in range(0, len(height)):
                if height[x] < y and l_wall_found:
                    potential_add += 1
                elif height[x] >= y and not l_wall_found:
                    l_wall_found = True
                elif height[x] >= y and l_wall_found:
                    output += potential_add
                    potential_add = 0

        return output
