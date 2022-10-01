from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = []
        r = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    c.append(j)
                    r.append(i)

        for i in range(len(matrix)):
            for j in c:
                matrix[i][j] = 0

        for i in r:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
