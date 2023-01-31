from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = m - 1

        for i in range(m):
            for j in range(m):
                if i == j or i + j == n:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True


grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
grid = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]

print(Solution().checkXMatrix(grid))
