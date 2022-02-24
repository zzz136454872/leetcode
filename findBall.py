from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, z):
            if x >= m:
                return y

            if y < 0 or y >= n:
                return -1

            if grid[x][y] == 1:
                if z == 0:
                    return dfs(x, y + 1, 3)

                if z == 2:
                    return -1

                return dfs(x + 1, y, 0)
            else:
                if z == 0:
                    return dfs(x, y - 1, 2)

                if z == 2:
                    return dfs(x + 1, y, 0)

                return -1

        out = []

        for i in range(n):
            out.append(dfs(0, i, 0))

        return out


grid = [[-1]]
grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1]]

print(Solution().findBall(grid))
