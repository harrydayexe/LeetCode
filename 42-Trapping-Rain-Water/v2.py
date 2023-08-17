from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_indices = [i for i, x in enumerate(height) if x == max(height)]
        mid_sum = self.middle_sum(height, tallest_indices)

        first_index = tallest_indices[0]
        last_index = tallest_indices[-1]
        left_to_first = self.end_to_middle_sum(height, range(0, first_index))
        right_to_end = self.end_to_middle_sum(height, range(len(height)-1, last_index, -1))

        print(left_to_first)
        print(mid_sum)
        print(right_to_end)
        return mid_sum + left_to_first + right_to_end


    def middle_sum(self, height: List[int], tallest_indices: List[int]) -> int:
        tallest = max(height)
        start = tallest_indices[0]
        end = tallest_indices[-1]
        running_total = 0
        for i in range(start + 1, end):
            running_total += tallest - height[i]

        return running_total

    def end_to_middle_sum(self, height: List[int], indices_range: range) -> int:
        potential = 0
        tallest_l_wall = 0
        for x in indices_range:
            if height[x] > tallest_l_wall:
                tallest_l_wall = height[x]
            elif height[x] < tallest_l_wall:
                potential += tallest_l_wall - height[x]

        return potential