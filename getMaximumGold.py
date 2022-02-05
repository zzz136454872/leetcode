from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def search(x, y):
            if x < 0 or x >= m:
                return 0

            if y < 0 or y >= n:
                return 0
            tmp = grid[x][y]
            grid[x][y] = 0

            if tmp == 0:
                return 0
            out = max(search(x + 1, y), search(x - 1, y), search(x, y + 1),
                      search(x, y - 1)) + tmp
            grid[x][y] = tmp

            return out

        out = 0

        for i in range(m):
            for j in range(n):
                out = max(out, search(i, j))

        return out


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(Solution().getMaximumGold(grid))
