from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mem = [True for i in range(m)]

        for i in range(n - 1):
            nmem = [False for i in range(m)]

            for j in range(m):
                if j < n - 1 and mem[j +
                                     1] and grid[j][i + 1] > grid[j + 1][i]:
                    nmem[j] = True
                elif mem[j] and grid[j][i + 1] > grid[j][i]:
                    nmem[j] = True
                elif j > 0 and mem[j - 1] and grid[j][i + 1] > grid[j - 1][i]:
                    nmem[j] = True

            if not any(nmem):
                return i
            mem = nmem

        return n - 1


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
print(Solution().maxMoves(grid))
