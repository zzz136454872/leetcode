from typing import List


# 最小高度树
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for i in range(n)]

        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        queue = []

        for i in range(n):
            if len(adj[i]) <= 1:
                queue.append(i)
        pre_queue = queue

        while len(queue) > 0:
            pre_queue = queue
            queue = []
            queue

            for node in pre_queue:
                for np in adj[node]:
                    adj[np].remove(node)

                    if len(adj[np]) == 1:
                        queue.append(np)

        return pre_queue


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
n = 1
edges = []
sl = Solution()
print(sl.findMinHeightTrees(n, edges))
