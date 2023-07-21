from typing import List


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int,
                     y1: int, x2: int, y2: int) -> bool:
        d2 = 0

        if xCenter < x1:
            d2 += (xCenter - x1)**2
        elif xCenter > x2:
            d2 += (xCenter - x2)**2

        if yCenter < y1:
            d2 += (yCenter - y1)**2
        elif yCenter > y2:
            d2 += (yCenter - y2)**2

        return d2 <= radius**2


radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1
radius = 1
xCenter = 1
yCenter = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1
radius = 1
xCenter = 0
yCenter = 0
x1 = -1
y1 = 0
x2 = 0
y2 = 1
print(Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
