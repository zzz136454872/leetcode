from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]],
                           patience: List[int]) -> int:
        queue = deque([0])
        n = len(patience)
        distance = [1234567] * n
        distance[0] = 0
        adjList = [[] for _ in range(n)]

        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        while len(queue) > 0:
            now = queue.popleft()
            nd = distance[now] + 1

            for nxt in adjList[now]:
                if distance[nxt] > nd:
                    distance[nxt] = nd
                    queue.append(nxt)
        out = 0

        for i in range(1, n):
            d = 2 * distance[i]
            out = max(out, 2 * d - (d - 1) % patience[i] - 1)

        return out + 1


# d=2 p=1

edges = [[0, 1], [1, 2]]
patience = [0, 2, 1]
edges = [[0, 1], [0, 2], [1, 2]]
patience = [0, 10, 10]
print(Solution().networkBecomesIdle(edges, patience))
