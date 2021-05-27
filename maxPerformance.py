from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: [int],
                       k: int) -> int:
        table = [(efficiency[i], speed[i]) for i in range(len(speed))]
        table.sort(reverse=True)
        efficiTable = []
        out = 0
        sumSpeed = 0

        for i in range(len(speed)):
            if len(efficiTable) < k:
                heappush(efficiTable, table[i][1])
                sumSpeed += table[i][1]
            else:
                if table[i][1] > efficiTable[0]:
                    sumSpeed += table[i][1] - efficiTable[0]
                    heappop(efficiTable)
                    heappush(efficiTable, table[i][1])
            out = max(out, table[i][0] * sumSpeed)
        mod = 10**9 + 7

        return out % mod


sl = Solution()
n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2

n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 3

n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 4
print(sl.maxPerformance(n, speed, efficiency, k))
