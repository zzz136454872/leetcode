from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n

        for ind in indices:
            row[ind[0]] += 1
            col[ind[1]] += 1
        r0 = len([x for x in row if x % 2 == 0])
        r1 = m - r0
        c0 = len([x for x in col if x % 2 == 0])
        c1 = n - c0

        return r0 * c1 + r1 * c0


m = 2
n = 3
indices = [[0, 1], [1, 1]]
print(Solution().oddCells(m, n, indices))
