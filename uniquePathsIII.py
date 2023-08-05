from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        c0 = 0
        aa = len(grid)
        bb = len(grid[0])

        for i in range(aa):
            for j in range(bb):
                if grid[i][j] == 0:
                    c0 += 1
                elif grid[i][j] == 1:
                    sa = i
                    sb = j

        def dfs(a, b, k):
            if a < 0 or a >= aa or b < 0 or b >= bb or grid[a][b] == -1:
                return 0
            res = 0

            if grid[a][b] == 2:
                if k == 0:
                    return 1

                return 0
            v = grid[a][b]
            grid[a][b] = -1
            k -= 1
            res += dfs(a + 1, b, k)
            res += dfs(a - 1, b, k)
            res += dfs(a, b + 1, k)
            res += dfs(a, b - 1, k)
            grid[a][b] = v

            return res

        return dfs(sa, sb, c0 + 1)


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
grid = [[0, 1], [2, 0]]
print(Solution().uniquePathsIII(grid))
