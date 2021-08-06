from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        if n == 1:
            return 0
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        mem = set((q[0], q[1]) for q in queue)
        target = 2**n - 1

        while True:
            now = queue.popleft()

            if now[1] == target:
                return now[2]

            for nextPoint in graph[now[0]]:
                nextMask = now[1] | (1 << nextPoint)

                if nextMask == target:
                    return now[2] + 1

                if (nextPoint, nextMask) not in mem:
                    mem.add((nextPoint, nextMask))
                    queue.append((nextPoint, nextMask, now[2] + 1))


sl = Solution()
graph = [[1, 2, 3], [0], [0], [0]]
graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print(sl.shortestPathLength(graph))
