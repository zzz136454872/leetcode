from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        n = len(grid)
        visited = [[0] * n for i in range(n)]
        res = -1

        while len(queue) > 0:
            now = queue.popleft()

            if now[0] < 0 or now[1] < 0 or now[0] >= n or now[1] >= n:
                continue

            if grid[now[0]][now[1]] == 1:
                continue

            if visited[now[0]][now[1]] == 1:
                continue

            if now[0] == n - 1 and now[1] == n - 1:
                res = now[2]

                break
            visited[now[0]][now[1]] = 1
            queue.append((now[0], now[1] + 1, now[2] + 1))
            queue.append((now[0], now[1] - 1, now[2] + 1))
            queue.append((now[0] + 1, now[1], now[2] + 1))
            queue.append((now[0] + 1, now[1] + 1, now[2] + 1))
            queue.append((now[0] + 1, now[1] - 1, now[2] + 1))
            queue.append((now[0] - 1, now[1], now[2] + 1))
            queue.append((now[0] - 1, now[1] + 1, now[2] + 1))
            queue.append((now[0] - 1, now[1] - 1, now[2] + 1))

        return res


grid = [[0, 1], [1, 0]]
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
print(Solution().shortestPathBinaryMatrix(grid))
