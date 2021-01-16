from typing import *
import copy

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        n1=len(grid)
        n2=len(grid[0])
        log=[False for i in range(len(hits))]
        for i in range(len(hits)):
            if not grid[hits[i][0]][hits[i][1]]:
                log[i]=True
            grid[hits[i][0]][hits[i][1]]=0

        def p2n(p0,p1):
            return p0*n2+p1
        
        # print(n1,n2)
        father=[i for i in range(n1*n2+1)]
        size=[1 for i in range(n1*n2+1)]
        size[n1*n2]=0

        def find(a):
            # print(a,father)
            if a==father[a]:
                return a
            father[a]=find(father[a])
            return father[a]

        def union(a,b):
            ra=find(a)
            rb=find(b)
            if ra>rb:
                father[rb]=ra
                size[ra]+=size[rb]
            if ra<rb:
                father[ra]=rb
                size[rb]+=size[ra]

        for i in range(n2):
            if grid[0][i]:
                union(i,n1*n2)
        
        for i in range(n1):
            for j in range(n2):
                if grid[i][j]:
                    if i>0 and grid[i-1][j]:
                        union(p2n(i,j),p2n(i-1,j))
                    if j>0 and grid[i][j-1]:
                        union(p2n(i,j),p2n(i,j-1))

        out=[0 for i in range(len(hits))]

        for k in range(len(hits)-1,-1,-1):
            if log[k]:
                continue
            i,j=hits[k]
            last=size[-1]
            if i==0:
                union(p2n(i,j),n1*n2)
            if i>0 and grid[i-1][j]:
                union(p2n(i,j),p2n(i-1,j))
            if j>0 and grid[i][j-1]:
                union(p2n(i,j),p2n(i,j-1))
            if i<n1-1 and grid[i+1][j]:
                union(p2n(i,j),p2n(i+1,j))
            if j<n2-1 and grid[i][j+1]:
                union(p2n(i,j),p2n(i,j+1))
            out[k]=max(0,size[-1]-last-1)
            grid[i][j]=1
            #print(grid,father,size)

        return out

sl=Solution()
grid=[[1],[1],[1],[1],[1]]
hits=[[3,0],[4,0],[1,0],[2,0],[0,0]]
print(sl.hitBricks(grid,hits))


