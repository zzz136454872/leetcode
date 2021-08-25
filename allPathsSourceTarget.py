from typing import List


class Solution:
    def dfs(self, start):
        if start == self.l - 1:
            return [[self.l - 1]]

        if self.log[start] != None:
            return self.log[start]
        out = []

        for end in self.graph[start]:
            tmp = self.dfs(end)

            for path in tmp:
                out.append([start] + path)
        self.log[start] = out

        return out

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.log = [None for i in range(len(graph))]
        self.graph = graph
        self.l = len(graph)

        return self.dfs(0)


inp = [[1, 2], [3], [3], []]
sl = Solution()
print(sl.allPathsSourceTarget(inp))
