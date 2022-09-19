from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sz = [1] * (n * n)
        parent = [i for i in range(n * n)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def linear(a, b):
            return a * n + b

        def find(a):
            if a == parent[a]:
                return a

            return find(parent[a])

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if sz[a] > sz[b]:
                sz[a] += sz[b]
                parent[b] = a
            else:
                sz[b] += sz[a]
                parent[a] = b

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if i > 0 and grid[i - 1][j] == 1:
                        union(linear(i, j), linear(i - 1, j))

                    if j > 0 and grid[i][j - 1] == 1:
                        union(linear(i, j), linear(i, j - 1))
        res = max(sz)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    total = 1
                    root = set()

                    for d in dirs:
                        x = i + d[0]
                        y = j + d[1]

                        if x >= 0 and x < n and y >= 0 and y < n and grid[x][
                                y] == 1:
                            idx = linear(x, y)
                            # print('idx',idx)
                            r = find(idx)

                            if r not in root:
                                total += sz[r]
                                root.add(r)
                    res = max(total, res)

        return res


grid = [[1, 0], [0, 1]]
grid = [[1, 1], [1, 0]]
grid = [[1, 1], [1, 1]]
print(Solution().largestIsland(grid))
