from typing import List


class Solution:
    def differenceOfDistinctValues(self,
                                   grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tl = [[0] * n]
        mem = [set() for i in range(n)]

        for i in range(1, m):
            tmp = [0]

            for j in range(1, n):
                mem[j].add(grid[i - 1][j - 1])
                tmp.append(len(mem[j]))
            mem.pop()
            mem.insert(0, set())
            tl.append(tmp)
        mem = [set() for i in range(n)]
        br = []

        for i in range(m - 2, -1, -1):
            tmp = []

            for j in range(0, n - 1):
                mem[j].add(grid[i + 1][j + 1])
                tmp.append(len(mem[j]))
            mem.pop(0)
            mem.append(set())
            tmp.append(0)
            br.append(tmp)
        br = br[::-1]
        br.append([0] * n)

        return [[abs(br[i][j] - tl[i][j]) for j in range(n)] for i in range(m)]


grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
grid = [[1]]
print(Solution().differenceOfDistinctValues(grid))
