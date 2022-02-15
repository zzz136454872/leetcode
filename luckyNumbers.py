from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        lx = [min(row) for row in matrix]
        ly = [max([matrix[i][j] for i in range(m)]) for j in range(n)]

        out = []

        for i in range(m):
            tmp = lx[i]

            for j in range(n):
                t = matrix[i][j]

                if t == tmp and t == ly[j]:
                    out.append(t)

        return out


matrix = [[7, 8], [1, 2]]
matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(Solution().luckyNumbers(matrix))
