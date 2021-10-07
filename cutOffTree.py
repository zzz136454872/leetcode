from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])

        def loc2idx(r, c):
            return r * n + c

        total = m * n
        adjList = [[] for i in range(total)]
        mem = {}

        for i in range(m):
            for j in range(n):
                if not forest[i][j]:
                    continue

                if i > 0 and forest[i - 1][j]:
                    adjList[loc2idx(i, j)].append(loc2idx(i - 1, j))
                    adjList[loc2idx(i - 1, j)].append(loc2idx(i, j))

                if j > 0 and forest[i][j - 1]:
                    adjList[loc2idx(i, j)].append(loc2idx(i, j - 1))
                    adjList[loc2idx(i, j - 1)].append(loc2idx(i, j))

                if forest[i][j] > 1:
                    mem[forest[i][j]] = loc2idx(i, j)

        loc = 0
        target = sorted(mem.keys())
        out = 0

        def getDistance(start, end):
            if start == end:
                return 0
            visited = [False for i in range(total)]
            queue = deque([(start, 0)])
            visited[start] = True

            while len(queue) > 0:
                now = queue.popleft()

                for nextPoint in adjList[now[0]]:
                    if visited[nextPoint]:
                        continue

                    if nextPoint == end:
                        return now[1] + 1
                    visited[nextPoint] = True
                    queue.append((nextPoint, now[1] + 1))

            return -1

        for t in target:
            # print(loc,mem[t])
            tmp = getDistance(loc, mem[t])

            if tmp == -1:
                return -1
            loc = mem[t]
            out += tmp

        return out


forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]
forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]
print(Solution().cutOffTree(forest))
