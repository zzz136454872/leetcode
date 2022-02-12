from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # for i in range(m):
        #     for j in range(n):
        #         print(grid[i][j],end=' ')
        #     print()
        def check(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True

            if grid[x][y] == 0 or grid[x][y] == 2:
                return False

            if grid[x][y] == 3:
                return True
            grid[x][y] = 2

            return check(x - 1, y) or check(x + 1, y) or check(
                x, y - 1) or check(x, y + 1)

        def mark(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return

            if grid[x][y] == 0 or grid[x][y] == 3:
                return
            grid[x][y] = 3
            mark(x - 1, y)
            mark(x + 1, y)
            mark(x, y - 1)
            mark(x, y + 1)

        for i in range(m):
            for j in range(n):
                if check(i, j):
                    mark(i, j)
        out = 0
        # print()
        # for i in range(m):
        #     for j in range(n):
        #         print(grid[i][j],end=' ')
        #     print()

        for i in range(m):
            for j in range(n):
                out += 1 if grid[i][j] == 2 else 0

        return out


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
grid = [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]
print(Solution().numEnclaves(grid))
