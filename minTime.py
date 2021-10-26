from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        adjList = [[] for i in range(n)]

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def travel(start, last):
            out = 0

            for nextPoint in adjList[start]:
                if nextPoint == last:
                    continue
                out += travel(nextPoint, start)

            if out > 0 or hasApple[start]:
                out += 2

            return out

        return max(travel(0, -1) - 2, 0)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
true = True
false = False
hasApple = [false, false, true, false, true, true, false]
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [false, false, true, false, false, true, false]
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [false, false, false, false, false, false, false]

print(Solution().minTime(n, edges, hasApple))
