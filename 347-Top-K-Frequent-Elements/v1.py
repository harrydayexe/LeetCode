from typing import List


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        counts = list(counts.items())

        sorted_counts = sorted(counts, key=lambda x: x[1], reverse=True)

        return [x for (x, n) in sorted_counts][:k]
