from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]],
                    time: List[int]) -> int:
        run = []
        prev = [set() for i in range(n)]
        nxt = [set() for i in range(n)]

        for r in relations:
            r[0] -= 1
            r[1] -= 1
            prev[r[1]].add(r[0])
            nxt[r[0]].add(r[1])
        t = 0

        for i in range(n):
            if len(prev[i]) == 0:
                heappush(run, (time[i], i))

        while len(run) > 0:
            now = heappop(run)
            t = now[0]

            for nn in nxt[now[1]]:
                prev[nn].remove(now[1])

                if len(prev[nn]) == 0:
                    heappush(run, (t + time[nn], nn))

        return t


n = 3
relations = [[1, 3], [2, 3]]
time = [3, 2, 5]
n = 5
relations = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
time = [1, 2, 3, 4, 5]
print(Solution().minimumTime(n, relations, time))
