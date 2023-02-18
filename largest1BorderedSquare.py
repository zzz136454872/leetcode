from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        right = [[0] * n for i in range(m)]
        down = [[0] * n for i in range(m)]

        for i in range(m):
            right[i][n - 1] = grid[i][n - 1]

            for j in range(n - 2, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = right[i][j + 1] + 1

        for j in range(n):
            down[m - 1][j] = grid[m - 1][j]

            for i in range(m - 2, -1, -1):
                if grid[i][j] == 1:
                    down[i][j] = down[i + 1][j] + 1

        print(right)
        print(down)

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                d = min(right[i][j], down[i][j])

                if d <= res:
                    continue
                # print(i,j,d)

                for k in range(d):
                    if down[i][j + k] > k and right[i + k][j] > k:
                        res = max(res, k + 1)

        return res * res


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
grid = [[1, 1, 0, 0]]
print(Solution().largest1BorderedSquare(grid))
