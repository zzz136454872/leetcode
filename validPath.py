from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int,
                  destination: int) -> bool:
        mem = [i for i in range(n)]

        def find(a):
            if mem[a] == a:
                return a

            return find(mem[a])

        def union(a, b):
            a = find(a)
            b = find(b)
            mem[max(a, b)] = min(a, b)

        for edge in edges:
            union(edge[0], edge[1])

        return find(source) == find(destination)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
print(Solution().validPath(n, edges, source, destination))
