from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)

        for x in grid:
            res += max(x)

        for j in range(n):
            res += max([x[j] for x in grid])

        for x in grid:
            for y in x:
                if y != 0:
                    res += 1

        return res


grid = [[1, 2], [3, 4]]
grid = [[2]]
grid = [[1, 0], [0, 2]]
grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().projectionArea(grid))
