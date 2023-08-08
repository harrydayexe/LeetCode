from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        groups = []
        for case in strs:
            found = False
            for i in range(len(groups)):
                if Solution.isAnagram(case, groups[i][0]):
                    groups[i].append(case)
                    found = True
                    break

            if not found:
                groups.append([case])

        return groups


    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t