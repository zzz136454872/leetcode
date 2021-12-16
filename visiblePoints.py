from math import acos, pi
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int,
                      location: List[int]) -> int:
        mem = []
        always = 0
        eps = 10**(-8)

        for p in points:
            dy = p[1] - location[1]
            dx = p[0] - location[0]
            d = (dx**2 + dy**2)**0.5

            if d < eps:
                always += 1

                continue
            angle1 = acos(dx / d)

            if dy < 0:
                angle1 = 2 * pi - angle1
            mem.append(angle1)
            mem.append(2 * pi + angle1)
        mem.sort()
        angle = angle * pi / 180
        out = 0
        j = 0
        # print(mem)
        # print(angle)

        for i in range(len(mem)):
            while j < len(mem) and mem[j] < mem[i] + angle + eps:
                j += 1
            out = max(out, j - i)

            if mem[i] > 2 * pi:
                break

        return out + always


points = [[2, 1], [2, 2], [3, 3]]
angle = 90
location = [1, 1]

points = [[2, 1], [2, 2], [3, 4], [1, 1]]
angle = 90
location = [1, 1]
points = [[1, 0], [2, 1]]
angle = 13
location = [1, 1]
print(Solution().visiblePoints(points, angle, location))
