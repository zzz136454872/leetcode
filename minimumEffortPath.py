from typing import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        y=len(heights)
        x=len(heights[0])
        parent=[i for i in range(x*y)]
        def find(a):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            aa=find(a)
            bb=find(b)
            parent[max(aa,bb)]=min(aa,bb)

        def reduction():
            for i in range(len(parent)):
                find(i)

        def hash1(i,j):
            return i*x+j

        def end():
            return find(hash1(0,0))==find(hash1(y-1,x-1))
        
        line=[]
        for i in range(y):
            for j in range(x):
                if i>0:
                    line.append((hash1(i-1,j),hash1(i,j),abs(heights[i][j]-heights[i-1][j])))
                if j>0:
                    line.append((hash1(i,j-1),hash1(i,j),abs(heights[i][j]-heights[i][j-1])))
        
        line.sort(key=lambda x:x[2])
        
        for l in line:
            union(l[0],l[1])
            if end():
                return l[2]

        return 0

sl=Solution()
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights=[[3]]
print(sl.minimumEffortPath(heights))
