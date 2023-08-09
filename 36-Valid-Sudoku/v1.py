from typing import List


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        for row in board:
            numbers = list(filter(".".__ne__, row))
            if len(numbers) != len(set(numbers)):
                return False

        for col_num in range(0, 9):
            numbers = [board[row_num][col_num] for row_num in range(0, 9) if board[row_num][col_num] != "."]
            if len(numbers) != len(set(numbers)):
                return False

        houses = [set() for i in range(0, 9)]
        for row_num in range(0, 9):
            for col_num in range(0, 9):
                if board[row_num][col_num] != ".":
                    pre_size = len(houses[(col_num//3) + (3*(row_num//3))])
                    houses[(col_num//3) + (3*(row_num//3))].add(board[row_num][col_num])
                    if pre_size == len(houses[(col_num//3) + (3*(row_num//3))]):
                        return False

        return True
