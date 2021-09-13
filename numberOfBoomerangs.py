from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        mem = [[0] * n for i in range(n)]

        out = 0

        for i in range(n):
            tmp = {}

            for j in range(n):
                mem[i][j] = (points[i][0] - points[j][0])**2 + (
                    points[i][1] - points[j][1])**2

            for j in range(n):
                tmp[mem[i][j]] = tmp.get(mem[i][j], 0) + 1
            # print(i,tmp)

            for idx in tmp:
                out += tmp[idx] * (tmp[idx] - 1)

        # print(mem)

        return out


points = [[0, 0], [1, 0], [2, 0]]
points = [[1, 1], [2, 2], [3, 3]]
points = [[1, 1]]
points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]

print(Solution().numberOfBoomerangs(points))
