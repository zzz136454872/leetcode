from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        mem = [[0] * n for i in range(m)]
        queue = []

        for i in range(m):
            queue.append([i, 0])

        for j in range(1, n):
            queue.append([0, j])

        def bfs(flag):
            while len(queue) > 0:
                now = queue.pop()

                if mem[now[0]][now[1]] & flag != 0:
                    continue
                mem[now[0]][now[1]] |= flag

                if now[0] > 0 and heights[now[0] - 1][now[1]] >= heights[
                        now[0]][now[1]]:
                    queue.append([now[0] - 1, now[1]])

                if now[0] < m - 1 and heights[now[0] + 1][now[1]] >= heights[
                        now[0]][now[1]]:
                    queue.append([now[0] + 1, now[1]])

                if now[1] > 0 and heights[now[0]][now[1] - 1] >= heights[
                        now[0]][now[1]]:
                    queue.append([now[0], now[1] - 1])

                if now[1] < n - 1 and heights[now[0]][now[1] + 1] >= heights[
                        now[0]][now[1]]:
                    queue.append([now[0], now[1] + 1])

        bfs(1)

        for i in range(m):
            queue.append([i, n - 1])

        for j in range(n - 1):
            queue.append([m - 1, j])
        bfs(2)
        res = []

        for i in range(m):
            for j in range(n):
                if mem[i][j] == 3:
                    res.append([i, j])

        return res


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]]
heights = [[2, 1], [1, 2]]
print(Solution().pacificAtlantic(heights))
