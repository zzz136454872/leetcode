from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]],
                            target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        rr = len(matrix)
        rc = len(matrix[0])
        mr = rr // 2
        mc = rc // 2

        if matrix[mr][mc] > target:
            return self.findNumberIn2DArray(
                [matrix[i][:mc]
                 for i in range(mr)], target) or self.findNumberIn2DArray(
                     [matrix[i][:mc] for i in range(mr, rr)],
                     target) or self.findNumberIn2DArray(
                         [matrix[i][mc:rc] for i in range(mr)], target)
        elif matrix[mr][mc] < target:
            return self.findNumberIn2DArray([
                matrix[i][mc + 1:] for i in range(mr + 1, rr)
            ], target) or self.findNumberIn2DArray(
                [matrix[i][mc + 1:]
                 for i in range(mr + 1)], target) or self.findNumberIn2DArray(
                     [matrix[i][:mc + 1] for i in range(mr + 1, rr)], target)

        if matrix[mr][mc] == target:
            return True


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
target = 20

print(Solution().findNumberIn2DArray(matrix, target))
