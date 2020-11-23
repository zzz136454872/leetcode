from typing import *

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        points.sort(key=lambda x:(x[1],x[0]))
        out=1
        loc=1
        shoot_loc=points[0][1]
        while loc<len(points):
            while loc<len(points) and points[loc][0]<=shoot_loc:
                loc+=1
            if loc<len(points):
                shoot_loc=points[loc][1]
                loc+=1
                out+=1
        return out

sl=Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
print(sl.findMinArrowShots(points))
