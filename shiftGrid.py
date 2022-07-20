from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = []

        for row in grid:
            tmp.extend(row)
        k %= len(tmp)
        tmp = tmp[-k:] + tmp[:-k]
        n = len(grid[0])
        res = []

        for i in range(len(tmp) // n):
            res.append(tmp[n * i:n * (i + 1)])

        return res


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 9
print(Solution().shiftGrid(grid, k))
