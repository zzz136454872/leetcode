from typing import *


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 2:
            return True
        queue = [0]
        log = [0 for i in range(len(graph))]
        log[0] = 1

        while len(queue) > 0 or log.count(0) > 0:
            if len(queue) == 0:
                i = 0

                while log[i] != 0:
                    i += 1
                log[i] = 1
                queue.append(i)
            node = queue[0]
            del queue[0]

            for node2 in graph[node]:
                if log[node] == log[node2]:
                    return False

                if log[node2] == 0:
                    queue.append(node2)
                    log[node2] = log[node] ^ 3

        return True


graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9],
         [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]
sl = Solution()
print(sl.isBipartite(graph))
