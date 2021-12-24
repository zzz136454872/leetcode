from heapq import heappop, heappush
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        out = 0
        heap = []

        for i in range(len(days)):
            if apples[i] > 0:
                heappush(heap, [days[i] + i, apples[i]])

            while len(heap) > 0 and heap[0][0] <= i:
                heappop(heap)

            if len(heap) > 0:
                out += 1
                heap[0][1] -= 1

                if heap[0][1] == 0:
                    heappop(heap)
        now = len(days)

        while len(heap) > 0:
            tmp = heappop(heap)

            if tmp[0] - now <= tmp[1]:
                out += tmp[0] - now
                now = tmp[0]
            else:
                out += tmp[1]
                now += tmp[1]

        return out


apples = [1, 2, 3, 5, 2]
days = [3, 2, 1, 4, 2]
apples = [3, 0, 0, 0, 0, 2]
days = [3, 0, 0, 0, 0, 2]
print(Solution().eatenApples(apples, days))
