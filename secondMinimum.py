from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int,
                      change: int) -> int:
        time1 = [-1 for i in range(n)]
        time2 = [-1 for i in range(n)]
        adjList = [[] for i in range(n)]

        for edge in edges:
            adjList[edge[0] - 1].append(edge[1] - 1)
            adjList[edge[1] - 1].append(edge[0] - 1)
        queue = deque([(0, 0)])
        rounds = 0

        while len(queue) > 0:
            tmp = queue.popleft()

            if tmp[0] == n - 1:
                if time1[-1] > 0:
                    if tmp[1] > time1[-1]:
                        rounds = tmp[1]

                        break
                else:
                    time1[-1] = tmp[1]

                    for last in adjList[tmp[0]]:
                        queue.append((last, tmp[1] + 1))
            else:
                if time1[tmp[0]] == -1:
                    time1[tmp[0]] = tmp[1]

                    for last in adjList[tmp[0]]:
                        queue.append((last, tmp[1] + 1))
                elif time2[tmp[0]] == -1 and tmp[1] > time1[tmp[0]]:
                    time2[tmp[0]] = tmp[1]

                    for last in adjList[tmp[0]]:
                        queue.append((last, tmp[1] + 1))

        out = 0

        for i in range(rounds):
            if (out // change) % 2 == 1:
                out += change - out % change
            out += time

        return out


n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
n = 2
edges = [[1, 2]]
time = 3
change = 2
print(Solution().secondMinimum(n, edges, time, change))
