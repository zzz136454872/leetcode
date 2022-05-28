from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int,
                     target: int) -> float:
        adjList = [[] for _ in range(n + 1)]

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        fromPoint = [-1] * (n + 1)
        stack = [1]

        while len(stack) > 0:
            now = stack.pop()

            if now == target:
                break

            for np in adjList[now]:
                if np == 1 or fromPoint[np] != -1:
                    continue
                fromPoint[np] = now
                stack.append(np)

        path = [target]
        p = target

        while p != 1:
            p = fromPoint[p]
            path.append(p)

        if len(path) > t + 1:

            return 0.0

        if len(path) < t + 1 and (len(adjList[target]) > 1
                                  or target == 1 and len(adjList[target]) > 0):

            return 0.0

        k = 1

        if len(adjList[1]) > 0:
            k *= 1 / len(adjList[1])

        for p in path[1:len(path) - 1]:
            if len(adjList[p]) > 1:
                k *= 1 / (len(adjList[p]) - 1)

        return k


n = 7
edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
t = 2
target = 4
target = 7

n = 3
edges = [[1, 2], [2, 3]]
t = 1
target = 2

n = 9
edges = [[2, 1], [3, 2], [4, 3], [5, 3], [6, 5], [7, 3], [8, 4], [9, 5]]
t = 9
target = 1
print(Solution().frogPosition(n, edges, t, target))
