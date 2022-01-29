from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        out = [[0 if isWater[i][j] == 1 else 12345 for j in range(m)]
               for i in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(m):
                if out[i][j] == 0:
                    queue.append((i, j))

        while len(queue) > 0:
            now = queue.popleft()
            i = now[0]
            j = now[1]
            h = out[i][j] + 1

            if i > 0 and out[i - 1][j] > h:
                out[i - 1][j] = h
                queue.append((i - 1, j))

            if j > 0 and out[i][j - 1] > h:
                out[i][j - 1] = h
                queue.append((i, j - 1))

            if i < n - 1 and out[i + 1][j] > h:
                out[i + 1][j] = h
                queue.append((i + 1, j))

            if j < m - 1 and out[i][j + 1] > h:
                out[i][j + 1] = h
                queue.append((i, j + 1))

        return out


isWater = [[0, 1], [0, 0]]
isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(Solution().highestPeak(isWater))
