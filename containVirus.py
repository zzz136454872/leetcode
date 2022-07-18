from collections import deque
from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        res = 0
        m = len(isInfected)
        n = len(isInfected[0])
        nxts = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while True:
            neighbors = list()
            walls = list()

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        queue = deque([(i, j)])
                        neighbor = set()
                        idx = len(neighbors) + 1
                        wall = 0
                        isInfected[i][j] = -idx

                        while len(queue) > 0:
                            x, y = queue.popleft()

                            for nxt in nxts:
                                nx = x + nxt[0]
                                ny = y + nxt[1]

                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        wall += 1
                                        neighbor.add((nx, ny))
                                    elif isInfected[nx][ny] == 1:
                                        queue.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                        neighbors.append(neighbor)
                        walls.append(wall)

            if len(neighbors) == 0:
                break

            idx = 0

            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            res += walls[idx]

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] == -idx - 1:
                            isInfected[i][j] = 2
                        else:
                            isInfected[i][j] = 1

            for i in range(len(neighbors)):
                if i == idx:
                    continue

                for loc in neighbors[i]:
                    isInfected[loc[0]][loc[1]] = 1

            if len(neighbors) == 1:
                break

        return res


isInfected = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
isInfected = [[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
isInfected = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 0, 0, 0, 0, 0]]

print(Solution().containVirus(isInfected))
