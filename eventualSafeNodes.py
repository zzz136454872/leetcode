import collections
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        inNode = [[] for i in range(n)]
        outDegree = [0] * n
        queue = collections.deque()

        for i in range(n):
            if len(graph[i]) == 0:
                queue.append(i)
            else:
                outDegree[i] = len(graph[i])

                for j in graph[i]:
                    inNode[j].append(i)
        out = []

        while queue:
            now = queue.popleft()
            out.append(now)

            for j in inNode[now]:
                outDegree[j] -= 1

                if not outDegree[j]:
                    queue.append(j)

        return sorted(out)


sl = Solution()
graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(sl.eventualSafeNodes(graph))
