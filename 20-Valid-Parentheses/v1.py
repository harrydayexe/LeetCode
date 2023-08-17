class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {")": "(", "]": "[", "}": '{'}
        for letter in s:
            if letter not in closers:
                stack.append(letter)
            elif not stack or stack.pop() != closers[letter]:
                return False

        return not stack
