from heapq import heappop, heappush
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        heap = [(2, 0, 0)]
        res = set()

        if x == 1:
            x = 10**6 + 1

        if y == 1:
            y = 10**6 + 1

        while heap[0][0] <= bound:
            now = heappop(heap)

            if now in res:
                continue
            res.add(now)
            heappush(heap, (now[0] + x**now[1] * (x - 1), now[1] + 1, now[2]))
            heappush(heap, (now[0] + y**now[2] * (y - 1), now[1], now[2] + 1))

        return list(set(a[0] for a in res))


x = 2
y = 3
bound = 10
x = 3
y = 5
bound = 15
print(Solution().powerfulIntegers(x, y, bound))
