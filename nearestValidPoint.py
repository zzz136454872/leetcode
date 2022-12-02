from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        m=12345
        res=-1
        d=m
        for i in range(len(points)):
            dd=m
            if points[i][0]==x:
                dd=abs(points[i][1]-y)
            elif points[i][1]==y:
                dd=abs(points[i][0]-x)
            if dd<d:
                d=dd
                res=i
                
        return res if d!=m else -1

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
x = 3
y = 4
points = [[3,4]]
x = 3
y = 4
points = [[2,3]]
print(Solution().nearestValidPoint(x,y,points))

