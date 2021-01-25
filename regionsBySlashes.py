from typing import *

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        y=len(grid)
        x=len(grid[0])
        parent=[i for i in range(4*x*y)]
        
        def find(a):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            aa=find(a)
            bb=find(b)
            parent[max(aa,bb)]=min(aa,bb)
        
        def getIndex(y1,x1,i):
            return 4*(y1*x+x1)+i

        def reduction():
            for i in range(len(parent)):
                find(i)
        
        for i in range(y):
            for j in range(x):
                # print(i,j)
                if i>0:
                    union(getIndex(i,j,0),getIndex(i-1,j,2))
                if j>0:
                    union(getIndex(i,j,3),getIndex(i,j-1,1))
                if grid[i][j]==' ':
                    union(getIndex(i,j,0),getIndex(i,j,1))
                    union(getIndex(i,j,0),getIndex(i,j,2))
                    union(getIndex(i,j,0),getIndex(i,j,3))
                elif grid[i][j]=='\\':
                    union(getIndex(i,j,0),getIndex(i,j,1))
                    union(getIndex(i,j,2),getIndex(i,j,3))
                elif grid[i][j]=='/':
                    union(getIndex(i,j,0),getIndex(i,j,3))
                    union(getIndex(i,j,1),getIndex(i,j,2))
        reduction()
        # print(parent)
        return len(set(parent))

sl=Solution()
inp=[ "\\/", "/\\" ]
print(sl.regionsBySlashes(inp))
            
