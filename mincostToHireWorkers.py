import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             k: int) -> float:
        n = len(quality)
        worker = [(wage[i] / quality[i], quality[i], wage[i])
                  for i in range(n)]
        worker.sort()
        heap = []

        for i in range(k - 1):
            heapq.heappush(heap, -worker[i][1])
        total = -sum(heap)

        # print(heap)
        # print(worker)

        ans = 123456789

        for i in range(k - 1, n):
            total += worker[i][1]
            heapq.heappush(heap, -worker[i][1])
            # print(i,total,worker[i][2]/worker[i][1])
            ans = min(ans, total * worker[i][2] / worker[i][1])
            total += heapq.heappop(heap)

        return ans


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(Solution().mincostToHireWorkers(quality, wage, k))
