from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int],
                       load: List[int]) -> List[int]:
        busy = []
        available = [i for i in range(k)]
        heapify(available)
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]
            duration = load[i]
            end = time + duration

            while len(busy) > 0 and busy[0][0] <= time:
                loc = heappop(busy)[1]
                heappush(available, i + (loc - i) % k)

            if len(available) > 0:
                loc = heappop(available) % k
                count[loc] += 1
                heappush(busy, (end, loc))
        m = max(count)

        return [i for i in range(k) if count[i] == m]


k = 2
arrival = [0, 10]
load = [2, 2]
k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]
k = 3
arrival = [1, 2, 3, 4]
load = [1, 2, 1, 2]
k = 3
arrival = [1, 2, 3]
load = [10, 12, 11]
k = 3
arrival = [1, 2, 3, 4, 8, 9, 10]
load = [5, 2, 10, 3, 1, 2, 2]
k = 1
arrival = [1]
load = [1]
print(Solution().busiestServers(k, arrival, load))
