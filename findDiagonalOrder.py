from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []

        for k in range(m + n - 1):
            if k % 2 != 0:
                for i in range(max(0, k - n + 1), min(m, k + 1)):
                    res.append(mat[i][k - i])
            else:
                for i in range(min(m - 1, k), max(-1, k - n), -1):
                    res.append(mat[i][k - i])

        return res


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1, 2], [3, 4]]
print(Solution().findDiagonalOrder(mat))
