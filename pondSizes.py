from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        n = len(land)
        m = len(land[0])

        def paint(a, b):
            if a < 0 or b < 0 or a >= n or b >= m or land[a][b] != 0:
                return 0
            land[a][b] = -1

            return 1 + paint(a + 1, b) + paint(a + 1, b - 1) +\
                paint(a + 1, b + 1) + paint(a, b - 1) + paint(a, b + 1) +\
                paint(a - 1, b) + paint(a - 1, b - 1) + paint(a - 1, b + 1)

        res = list()

        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    res.append(paint(i, j))

        return sorted(res)


inp = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]

print(Solution().pondSizes(inp))
