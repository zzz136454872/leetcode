from typing import *


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        def f(a):
            if a == 0:
                return "Gold Medal"

            if a == 1:
                return "Silver Medal"

            if a == 2:
                return "Bronze Medal"

            return str(a + 1)

        n = len(nums)
        log = [(nums[i], i) for i in range(n)]
        log.sort(reverse=True)  # ascending
        log = [(log[i][1], i) for i in range(n)]
        log.sort()
        out = [f(a[1]) for a in log]

        return out


inp = [5, 4, 3, 2, 1]
sl = Solution()
print(sl.findRelativeRanks(inp))
