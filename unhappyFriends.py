from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]],
                       pairs: List[List[int]]) -> int:
        rank = [[0] * n for i in range(n)]

        for i in range(n):
            for j in range(n - 1):
                rank[i][preferences[i][j]] = j
        mem = [True for i in range(n)]
        n //= 2

        for i in range(n - 1):
            for j in range(i + 1, n):
                x = pairs[i][0]
                y = pairs[i][1]
                u = pairs[j][0]
                v = pairs[j][1]
                xy = rank[x][y]
                yx = rank[y][x]
                uv = rank[u][v]
                vu = rank[v][u]
                xu = rank[x][u]
                ux = rank[u][x]
                xv = rank[x][v]
                vx = rank[v][x]
                yv = rank[y][v]
                vy = rank[v][y]
                yu = rank[y][u]
                uy = rank[u][y]

                if xu < xy and ux < uv:
                    mem[x] = False
                    mem[u] = False

                if xv < xy and vx < vu:
                    mem[x] = False
                    mem[v] = False

                if yu < yx and uy < uv:
                    mem[y] = False
                    mem[u] = False

                if yv < yx and vy < vu:
                    mem[y] = False
                    mem[v] = False

        return mem.count(False)


sl = Solution()
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
n = 6
preferences = [[2, 1, 4, 5, 3], [4, 0, 3, 2, 5], [3, 0, 4, 1, 5],
               [2, 4, 5, 0, 1], [5, 1, 2, 3, 0], [2, 0, 3, 1, 4]]
pairs = [[0, 5], [4, 3], [2, 1]]

print(sl.unhappyFriends(n, preferences, pairs))
