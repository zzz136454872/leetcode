from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        t = [dist[i] / speed[i] for i in range(n)]
        t.sort()

        for i in range(n):
            if t[i] <= i:
                return i

        return n


dist = [1, 3, 4]
speed = [1, 1, 1]

dist = [1, 1, 2, 3]
speed = [1, 1, 1, 1]

dist = [3, 2, 4]
speed = [5, 3, 2]
print(Solution().eliminateMaximum(dist, speed))
