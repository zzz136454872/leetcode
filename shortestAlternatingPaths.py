from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]],
                                 blueEdges: List[List[int]]) -> List[int]:
        big = 200
        dis = [[big] * n, [big] * n]
        link = [[set() for i in range(n)], [set() for i in range(n)]]

        for s, e in redEdges:
            link[0][s].add(e)

        for s, e in blueEdges:
            link[1][s].add(e)

        queue = deque([(0, 0, 0), (0, 0, 1)])

        while len(queue) > 0:
            p, d, c = queue.popleft()

            if dis[c][p] <= d:
                continue
            dis[c][p] = d

            for nxt in link[1 - c][p]:
                queue.append((nxt, d + 1, 1 - c))

        return [
            min(dis[0][i], dis[1][i])
            if min(dis[0][i], dis[1][i]) != big else -1 for i in range(n)
        ]


n = 3
red_edges = [[0, 1], [1, 2]]
blue_edges = []
n = 3
red_edges = [[0, 1]]
blue_edges = [[2, 1]]
n = 3
red_edges = [[1, 0]]
blue_edges = [[2, 1]]
n = 3
red_edges = [[0, 1], [0, 2]]
blue_edges = [[1, 0]]

n = 6
red_edges = [[4, 1], [3, 5], [5, 2], [1, 4], [4, 2], [0, 0], [2, 0], [1, 1]]
blue_edges = [[5, 5], [5, 0], [4, 4], [0, 3], [1, 0]]
print(Solution().shortestAlternatingPaths(n, red_edges, blue_edges))
