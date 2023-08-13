class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        s = s.upper()
        s = [letter for letter in s if letter.isalnum()]
        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return False
        return True
