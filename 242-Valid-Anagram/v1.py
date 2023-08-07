import string


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        # Not an anagram if different lengths
        if len(s) != len(t):
            return False

        s_count, t_count = {}, {}
        for letter in list(string.ascii_lowercase):
            s_count[letter] = 0
            t_count[letter] = 0

        for letter in s:
            s_count[letter] += 1

        for letter in t:
            t_count[letter] += 1

        return s_count == t_count
