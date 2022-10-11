from collections import defaultdict
from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        a = defaultdict(int)

        for d in demand:
            tmp = defaultdict(int)

            for letter in d:
                tmp[letter] += 1

            for k in tmp:
                a[k] = max(tmp[k], a[k])

        return sum(a.values())


demand = ["abc", "ab", "ac", "b"]
demand = ["acd", "bed", "accd"]
print(Solution().minNumBooths(demand))
