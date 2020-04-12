
from typing import *
inf=12345678
exp=0.000000001

def k(start,end):
    if start[0]==end[0]:
        return inf
    return (start[1]-end[1])/(start[0]-end[0])

def pointOnLine(start,end,point):
    if point[0]<min(start[0],end[0])-exp:
        return False
    if point[0]>max(start[0],end[0])+exp:
        return False
    if point[1]<min(start[1],end[1])-exp:
        return False
    if point[1]>max(start[1],end[1])+exp:
        return False
    return True
    
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        k1=k(start1,end1)
        k2=k(start2,end2)

        if k1==inf and k2!=inf:
            b2=start2[1]-k2*start2[0]
            point=[0,0]
            point[0]=start1[0]
            point[1]=k2*point[0]+b2
            print(k2,b2)

            if pointOnLine(start2,end2,point) and pointOnLine(start1,end2,point):
                return point
            return []
        
        if k1!=inf and k2==inf:
            b1=start1[1]-k1*start1[0]
            point=[0,0]
            point[0]=start2[0]
            point[1]=k1*point[0]+b1
            if pointOnLine(start1,end1,point) and pointOneLine(start2,end2,point):
                return point
            return []

        if k1==inf and k2==inf:
            if start1[0]!=start2[0]:
                return []
            if start1[1] > end1[1]:
                start1,end1=end1,start1
            if start2[1] > end2[1]:
                start2,end2=end2,start2
            if start1[1]<=start2[1]:
                if end1[1]<start2[1]:
                    return []
                return start2
            if start1[1]>end2[0]:
                return []
            return start1
        b2=start2[1]-k2*start2[0]
        b1=start1[1]-k1*start1[0]
        if k1==k2:
            if b1 != b2:
                return []
            if start1[0] > end1[0]:
                start1,end1=end1,start1
            if start2[0] > end2[0]:
                start2,end2=end2,start2
            if start1[0] > max(start2[0],end2[0]):
                return []
            if end1[0] < min(start2[0],end2[0]):
                return []
            if start1[0] < start2[0]:
                return start2
            else:
                return start1
        px=(b1-b2)/(k2-k1)
        py=(k2*b1-k1*b2)/(k2-k1)
        point=(px,py)
        if pointOnLine(start1,end1,point) and pointOnLine(start2,end2,point):
            return point
        return []
sl=Solution()
start1=[12, -55]
end1=[59, -60]
start2=[4, -55]
end2=[81, -62]

print(sl.intersection(start1,end1,start2,end2))


