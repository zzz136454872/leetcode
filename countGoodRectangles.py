from typing import *

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        log=[min(a,b) for a,b in rectangles]
        m=max(log)
        return [m==n for n in log].count(True)

sl=Solution()
rectangles = [[2,3],[3,7],[4,3],[3,7]]
print(sl.countGoodRectangles(rectangles))
