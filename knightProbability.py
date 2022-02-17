from typing import List


class Solution:
    def knightProbability(self, n: int, k: int, row: int,
                          column: int) -> float:
        mem = [[0] * n for _ in range(n)]
        mem[row][column] = 1

        def inside(x, y):
            return x >= 0 and y >= 0 and y < n and x < n

        directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1),
                      (-1, -2), (-2, -1)]

        for r in range(k):
            mem_new = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    tmp = mem[i][j]

                    if tmp == 0:
                        continue

                    for d in directions:
                        if inside(i + d[0], j + d[1]):
                            mem_new[i + d[0]][j + d[1]] += tmp * 0.125
            mem = mem_new

        return sum([sum(r) for r in mem])


n = 3
k = 2
row = 0
column = 0
n = 1
k = 0
row = 0
column = 0
print(Solution().knightProbability(n, k, row, column))
