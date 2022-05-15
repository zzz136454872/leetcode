from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return 0.5 * max([
            abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] +
                points[k][0] * points[i][1] - points[i][1] * points[j][0] -
                points[j][1] * points[k][0] - points[k][1] * points[i][0])
            for i in range(len(points) - 2)
            for j in range(i + 1, len(points) - 1)
            for k in range(j + 1, len(points))
        ])

points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(Solution().largestTriangleArea(points))
