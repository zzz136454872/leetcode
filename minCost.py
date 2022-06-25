from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        mem = [[0] * 3 for i in range(n)]

        for i in range(3):
            mem[0][i] = costs[0][i]

        for i in range(1, n):
            for j in range(3):
                m = 12345

                for k in range(3):
                    if j == k:
                        continue
                    m = min(m, mem[i - 1][k])
                mem[i][j] = m + costs[i][j]

        return min(mem[-1])


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
costs = [[7, 6, 2]]
print(Solution().minCost(costs))
