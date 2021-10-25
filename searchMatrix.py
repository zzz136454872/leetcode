from typing import List


# 不确定是哪一个
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = len(matrix)
        x = len(matrix[0])

        def idx2cord(idx):
            return (idx // x, idx % x)

        left = 0
        right = x * y - 1

        while left <= right:
            mid = (left + right) // 2
            cord = idx2cord(mid)

            if matrix[cord[0]][cord[1]] < target:
                left = mid + 1
            elif matrix[cord[0]][cord[1]] > target:
                right = mid - 1
            else:
                return True

        return False


# sl=Solution()
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 61
# print(sl.searchMatrix(matrix,target))


# 搜索二维矩阵 II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][-1] >= target:
                right = mid - 1
            else:
                left = mid + 1
        start = left

        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        end = left

        for i in range(start, end):
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    return True

        return False


sl = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5

matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20

print(sl.searchMatrix(matrix, target))
