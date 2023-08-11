from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        out = 0
        n = len(mat)

        for i in range(n):
            out += mat[i][i]
            out += mat[i][n - 1 - i]

        if n % 2 != 0:
            out -= mat[n // 2][n // 2]

        return out


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sl = Solution()
print(sl.diagonalSum(mat))
