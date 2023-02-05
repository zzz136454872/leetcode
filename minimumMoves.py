from collections import deque
from typing import List


# 不知道是哪个
class Solution1:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        i = 0
        res = 0

        while i < len(s):
            if s[i] == 'X':
                s[i] = '0'
                res += 1
                i += 1

                if i < len(s):
                    s[i] = '0'
                i += 1

                if i < len(s):
                    s[i] = '0'
            i += 1

        return res


# s = "XXX"
# s = "XXOX"
# s = "OOOO"
# print(Solution().minimumMoves(s))


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 1, 0, 0)])
        visited = set()
        n = len(grid)

        while len(queue) > 0:
            now = queue.popleft()
            k = now[:3]

            if k in visited:
                continue

            if k == (n - 1, n - 1, 0):
                return now[3]
            visited.add(k)

            if now[2] == 0:
                if now[0] < n - 1 and grid[now[0] + 1][
                        now[1] - 1] == 0 and grid[now[0] + 1][now[1]] == 0:
                    queue.append((now[0] + 1, now[1], 0, now[3] + 1))
                    queue.append((now[0] + 1, now[1] - 1, 1, now[3] + 1))

                if now[1] < n - 1 and grid[now[0]][now[1] + 1] == 0:
                    queue.append((now[0], now[1] + 1, 0, now[3] + 1))
            else:
                if now[0] < n - 1 and grid[now[0] + 1][now[1]] == 0:
                    queue.append((now[0] + 1, now[1], 1, now[3] + 1))

                if now[1] < n - 1 and grid[now[0] - 1][
                        now[1] + 1] == 0 and grid[now[0]][now[1] + 1] == 0:
                    queue.append((now[0], now[1] + 1, 1, now[3] + 1))
                    queue.append((now[0] - 1, now[1] + 1, 0, now[3] + 1))

        return -1


grid = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0]]

grid = [[0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0]]

print(Solution().minimumMoves(grid))
