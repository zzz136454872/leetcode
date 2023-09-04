from collections import deque
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int],
                            start: List[int], k: int) -> List[List[int]]:
        queue = deque([(start[0], start[1], 0)])
        possible = []
        m = len(grid)
        n = len(grid[0])
        visited = set()

        while len(queue) > 0:
            now = queue.popleft()

            if now[0] < 0 or now[0] >= m or now[1] < 0 or now[1] >= n:
                continue

            if grid[now[0]][now[1]] == 0:
                continue
            key = (now[0], now[1])

            if key in visited:
                continue
            visited.add(key)
            p = grid[now[0]][now[1]]

            if p >= pricing[0] and p <= pricing[1]:
                possible.append((now[2], p, now[0], now[1]))

            queue.append((now[0] + 1, now[1], now[2] + 1))
            queue.append((now[0] - 1, now[1], now[2] + 1))
            queue.append((now[0], now[1] + 1, now[2] + 1))
            queue.append((now[0], now[1] - 1, now[2] + 1))

        possible.sort()

        return [p[2:] for p in possible[:k]]


grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
pricing = [2, 5]
start = [0, 0]
k = 3
grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
pricing = [2, 3]
start = [2, 3]
k = 2
grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
pricing = [2, 3]
start = [0, 0]
k = 3
print(Solution().highestRankedKItems(grid, pricing, start, k))
