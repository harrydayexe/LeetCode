from typing import List
from operator import mul, sub, add, truediv


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }
        for token in tokens:
            if token in operator_map.keys():
                result = int(operator_map[token](stack[-2], stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
