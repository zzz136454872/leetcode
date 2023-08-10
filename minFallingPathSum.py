from typing import List


# 不知道是哪个
class Solution1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mem = matrix[0]

        if n == 1:
            return mem[0]

        for i in range(1, n):
            nmem = [min(mem[0], mem[1]) + matrix[i][0]]

            for j in range(1, n - 1):
                nmem.append(min(mem[j - 1], mem[j], mem[j + 1]) + matrix[i][j])
            nmem.append(min(mem[-1], mem[-2]) + matrix[i][-1])
            mem = nmem

        return min(mem)


# matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# matrix = [[-19, 57], [-40, -5]]
# print(Solution().minFallingPathSum(matrix))


# 1289. 下降路径最小和 II
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mem = grid[0]

        for i in range(1, n):
            newMem = grid[i].copy()
            mem = sorted([(mem[j], j) for j in range(n)])

            for j in range(n):
                if j != mem[0][1]:
                    newMem[j] += mem[0][0]
                else:
                    newMem[j] += mem[1][0]
            mem = newMem

        return min(mem)


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().minFallingPathSum(grid))
