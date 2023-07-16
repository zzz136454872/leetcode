from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda x: x[0] + x[2])
        time = time[::-1]
        print(time)
        waitLeft = [i for i in range(k)]
        heapify(waitLeft)
        waitRight = []
        workLeft = []
        workRight = []
        remind = n
        now = 0
        big = 12345678910

        while remind > 0 or len(workRight) > 0 or len(waitRight) > 0:
            while len(workLeft) > 0 and workLeft[0][0] <= now:
                p = heappop(workLeft)
                heappush(waitLeft, p[1])

            while len(workRight) > 0 and workRight[0][0] <= now:
                p = heappop(workRight)
                heappush(waitRight, p[1])

            if len(waitRight) > 0:
                p = heappop(waitRight)
                # print(p,'right to left', now)
                now += time[p][2]
                heappush(workLeft, [now + time[p][3], p])
            elif len(waitLeft) > 0 and remind > 0:
                remind -= 1
                p = heappop(waitLeft)
                # print(p,'left to right', now)
                now += time[p][0]
                heappush(workRight, [now + time[p][1], p])
            else:
                # print(now,workLeft[0][0] if len(workLeft)>0 else "void",workRight[0][0] if len(workRight)>0 else "void")
                now = big

                if len(workLeft) > 0:
                    now = workLeft[0][0]

                if len(workRight) > 0:
                    now = min(now, workRight[0][0])

        return now


n = 1
k = 3
time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]
n = 3
k = 2
time = [[1, 9, 1, 8], [10, 10, 10, 10]]
n = 10000
k = 1
time = [[1000, 1000, 1000, 1000]]
print(Solution().findCrossingTime(n, k, time))
