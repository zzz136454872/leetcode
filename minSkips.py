from math import ceil
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        dp = [0] * (n + 1)
        eps = 10**(-8)

        for i in range(n):
            ndp = [0] * (n + 1)

            for j in range(i + 2):
                ndp[0] = ceil(dp[0] - eps) + dist[i] / speed

                if j == i + 1:
                    ndp[j] = dp[j - 1] + dist[i] / speed
                else:
                    ndp[j] = min(
                        ceil(dp[j] - eps) + dist[i] / speed,
                        dp[j - 1] + dist[i] / speed)
            dp = ndp
            # print(dp)

        for j in range(n):
            if dp[j] - eps <= hoursBefore:
                return j

        return -1


dist = [1, 3, 2]
speed = 4
hoursBefore = 2
dist = [7, 3, 5, 5]
speed = 2
hoursBefore = 10
dist = [7, 3, 5, 5]
speed = 1
hoursBefore = 10
print(Solution().minSkips(dist, speed, hoursBefore))
