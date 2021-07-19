import math
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        out = 0
        out += math.ceil((rungs[0] - dist) / dist)

        for i in range(len(rungs) - 1):
            out += math.ceil((rungs[i + 1] - rungs[i] - dist) / dist)

        return out


sl = Solution()
rungs = [1, 3, 5, 10]
dist = 2
rungs = [3, 6, 8, 10]
dist = 3
rungs = [3, 4, 6, 7]
dist = 2
rungs = [5]
dist = 10
print(sl.addRungs(rungs, dist))
