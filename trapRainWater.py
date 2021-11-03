from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        water = [[12345678] * n for i in range(m)]

        for i in range(m):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            water[i][0] = 0
            water[i][n - 1] = 0

        for j in range(1, n - 1):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[m - 1][j], m - 1, j))
            water[0][j] = 0
            water[m - 1][j] = 0

        while len(heap) > 0:
            now = heappop(heap)
            nh = now[0]

            if now[1] > 0:
                if water[now[1] - 1][now[2]] + heightMap[now[1] - 1][
                        now[2]] > nh and water[now[1] - 1][now[2]] > 0:
                    water[now[1] - 1][now[2]] = max(
                        0, nh - heightMap[now[1] - 1][now[2]])
                    heappush(
                        heap,
                        (water[now[1] - 1][now[2]] +
                         heightMap[now[1] - 1][now[2]], now[1] - 1, now[2]))

            if now[1] < m - 1:
                if water[now[1] + 1][now[2]] + heightMap[now[1] + 1][
                        now[2]] > nh and water[now[1] + 1][now[2]] > 0:
                    water[now[1] + 1][now[2]] = max(
                        0, nh - heightMap[now[1] + 1][now[2]])
                    heappush(
                        heap,
                        (water[now[1] + 1][now[2]] +
                         heightMap[now[1] + 1][now[2]], now[1] + 1, now[2]))

            if now[2] > 0:
                if water[now[1]][now[2] - 1] + heightMap[now[1]][
                        now[2] - 1] > nh and water[now[1]][now[2] - 1] > 0:
                    water[now[1]][now[2] - 1] = max(
                        0, nh - heightMap[now[1]][now[2] - 1])
                    heappush(
                        heap,
                        (water[now[1]][now[2] - 1] +
                         heightMap[now[1]][now[2] - 1], now[1], now[2] - 1))

            if now[2] < n - 1:
                if water[now[1]][now[2] + 1] + heightMap[now[1]][
                        now[2] + 1] > nh and water[now[1]][now[2] + 1] > 0:
                    water[now[1]][now[2] + 1] = max(
                        0, nh - heightMap[now[1]][now[2] + 1])
                    heappush(
                        heap,
                        (water[now[1]][now[2] + 1] +
                         heightMap[now[1]][now[2] + 1], now[1], now[2] + 1))

        return sum(sum(w) for w in water)


heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
heightMap = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3],
             [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
# heightMap=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(Solution().trapRainWater(heightMap))
