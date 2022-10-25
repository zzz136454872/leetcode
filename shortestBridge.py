from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x = i
                    y = j

                    break
        queue = deque([(x, y)])
        queue2 = deque()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while len(queue) > 0:
            now = queue.popleft()

            if now[0] < 0 or now[0] >= n or now[1] < 0 or now[1] >= m:
                continue

            if grid[now[0]][now[1]] != 1:
                continue
            queue2.append((now[0], now[1], 0))
            grid[now[0]][now[1]] = -1

            for d in dirs:
                queue.append((now[0] + d[0], now[1] + d[1]))

        print(queue2)

        while len(queue2) > 0:
            now = queue2.popleft()
            print(now)

            for d in dirs:
                nxt = (now[0] + d[0], now[1] + d[1])

                if nxt[0] < 0 or nxt[0] >= n or nxt[1] < 0 or nxt[1] >= m:
                    continue

                if grid[nxt[0]][nxt[1]] == -1:
                    continue

                if grid[nxt[0]][nxt[1]] == 1:
                    return now[2]
                grid[nxt[0]][nxt[1]] = -1
                queue2.append((nxt[0], nxt[1], now[2] + 1))

        return -1


grid = [[0, 1], [1, 0]]
print(Solution().shortestBridge(grid))
