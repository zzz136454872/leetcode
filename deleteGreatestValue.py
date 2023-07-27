from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for g in grid:
            g.sort()

        return sum([
            max([grid[i][j] for i in range(len(grid))])
            for j in range(len(grid[0]))
        ])


grid = [[1, 2, 4], [3, 3, 1]]
grid = [[10]]
print(Solution().deleteGreatestValue(grid))
