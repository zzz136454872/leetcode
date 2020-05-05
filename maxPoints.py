from typing import *

def sameLine(p1,p2,p3):
    return (p1[0]-p2[0])*(p2[1]-p3[1])==(p2[0]-p3[0])*(p1[1]-p2[1])

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return len(points)
        samePoint=[1 for i in range(len(points))]
        for i in range(len(points)-1):
            j=i+1
            while j < len(points):
                if points[i][0]==points[j][0] and points[i][1]==points[j][1]:
                    del points[j]
                    del samePoint[j]
                    samePoint[i]+=1
                else:
                    j+=1
        if len(samePoint)==1:
            return samePoint[0]
        else:
            longest=max(samePoint)+1
        #print(points)
        #print(samePoint)
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                tmp=samePoint[i]+samePoint[j]
                for k in range(j+1,len(points)):
                    if sameLine(points[i],points[j],points[k]):
                        tmp+=samePoint[k]
                    #print(i,j,k,tmp)
                #print(tmp)
                if tmp>longest:
                    longest=tmp
        return longest

inp=[[1,1],[1,1],[2,2],[2,2]]

sl=Solution()
print(sl.maxPoints(inp))
                   
