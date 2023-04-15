from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}

        for p in paths:
            p[0] -= 1
            p[1] -= 1

            if p[0] > p[1]:
                adj[p[0]].append(p[1])
            else:
                adj[p[1]].append(p[0])
        color = [-1 for i in range(n)]

        for i in range(n):
            choose = {1, 2, 3, 4}

            for a in adj[i]:
                choose.discard(color[a])
            color[i] = choose.pop()

        return color


n = 3
paths = [[1, 2], [2, 3], [3, 1]]
n = 4
paths = [[1, 2], [3, 4]]
n = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
print(Solution().gardenNoAdj(n, paths))
