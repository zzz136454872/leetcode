from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(lambda: dict())
        MOD = 10**9 + 7
        BIG = 123456789012345
        dis = [BIG] * n
        dis[0] = 0

        for r in roads:
            adjList[r[0]][r[1]] = r[2]
            adjList[r[1]][r[0]] = r[2]

        visited = [False] * n
        paths = [0] * n
        paths[0] = 1

        heap = [(0, 0)]

        while len(heap) > 0:
            nowdis, node = heappop(heap)

            if visited[node]:
                continue
            visited[node] = True

            for nxt in adjList[node]:
                nd = adjList[node][nxt] + nowdis

                if nd > dis[nxt]:
                    continue
                elif nd == dis[nxt]:
                    paths[nxt] = (paths[nxt] + paths[node]) % MOD
                else:
                    paths[nxt] = paths[node]
                    dis[nxt] = nd
                    heappush(heap, (nd, nxt))

        return paths[-1]


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1],
         [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
n = 2
roads = [[1, 0, 10]]

print(Solution().countPaths(n, roads))
