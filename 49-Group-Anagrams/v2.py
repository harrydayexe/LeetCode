import collections
from typing import List
import collections


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            ans[tuple(count)].append(s)

        return ans.values()