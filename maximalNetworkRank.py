from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [set() for i in range(n)]

        for i in range(len(roads)):
            adj[roads[i][0]].add(i)
            adj[roads[i][1]].add(i)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(adj[i] | adj[j]))

        return res


n = 4
roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
n = 5
roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
print(Solution().maximalNetworkRank(n, roads))
