from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p2 = 0
        p1 = 0

        for c in cost:
            p1, p2 = min(p1, p2) + c, p1

        return min(p1, p2)


cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
