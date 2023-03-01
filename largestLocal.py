from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        r1 = []
        r2 = []

        for g in grid:
            tmp = []

            for i in range(1, len(g) - 1):
                tmp.append(max(g[i - 1], g[i], g[i + 1]))
            r1.append(tmp)

        for i in range(1, len(r1) - 1):
            tmp = []

            for j in range(len(r1[0])):
                tmp.append(max(r1[i - 1][j], r1[i][j], r1[i + 1][j]))
            r2.append(tmp)

        return r2


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]
print(Solution().largestLocal(grid))
