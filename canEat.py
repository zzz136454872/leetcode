from typing import *

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        cans=len(candiesCount)
        qus=len(queries)
        s1=[0 for i in range(cans+1)]
        tmp=0
        for i in range(cans):
            tmp+=candiesCount[i]
            s1[i+1]=tmp

        out=[True for i in range(qus)]
        print(s1)
        for i in range(qus):
            if queries[i][1]>=s1[queries[i][0]+1]:
                out[i]=False
            if s1[queries[i][0]]>=queries[i][2]*(queries[i][1]+1):
                out[i]=False
        return out

sl=Solution()
candiesCount = [5,2,6,4,1]
queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
print(sl.canEat(candiesCount,queries))
            


        

