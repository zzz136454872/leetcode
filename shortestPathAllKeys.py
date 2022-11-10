from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        mem = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        allmask = 0
        queue = deque()

        def l2n(a):
            return ord(a) - ord('a')

        def L2n(a):
            return ord(a) - ord('A')

        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    allmask |= (1 << l2n(grid[i][j]))
                elif grid[i][j] == '@':
                    queue.append((i, j, 0, 0))

        if allmask == 0:
            return 0

        while len(queue) > 0:
            a = queue.popleft()

            for d in dirs:
                x = a[0] + d[0]
                y = a[1] + d[1]

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                if grid[x][y] == '#':
                    continue

                if grid[x][y].isupper() and a[2] & (1 << L2n(grid[x][y])) == 0:
                    continue
                mask = a[2]

                if grid[x][y].islower():
                    mask |= (1 << l2n(grid[x][y]))

                if (x, y, mask) in mem:
                    continue

                if mask == allmask:
                    return a[3] + 1
                mem.add((x, y, mask))
                queue.append((x, y, mask, a[3] + 1))

        return -1


grid = ["@.a.#", "###.#", "b.A.B"]
grid = ["@..aA", "..B#.", "....b"]
grid = ["@Aa"]
grid = [".@aA"]
print(Solution().shortestPathAllKeys(grid))
