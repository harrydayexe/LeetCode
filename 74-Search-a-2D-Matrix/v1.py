from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower, upper = 0, len(matrix) - 1

        while lower <= upper:
            row = (upper + lower) // 2
            if target > matrix[row][-1]:
                lower = row + 1
            elif target < matrix[row][0]:
                upper = row - 1
            else:
                break

        if not (lower <= upper):
            return False

        row = (lower + upper) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
