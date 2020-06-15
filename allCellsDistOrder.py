from typing import *

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        queue=[]
        visited=[[False for j in range(C)] for i in range(R)]
        visited[r0][c0]=True
        queue.append([r0,c0])
        out=[[r0,c0]]
        while len(queue)>0:
            r,c=queue.pop(0)
            if r>0 and not visited[r-1][c]:
                visited[r-1][c]=True
                queue.append([r-1,c])
                out.append([r-1,c])
            if c>0 and not visited[r][c-1]:
                visited[r][c-1]=True
                queue.append([r,c-1])
                out.append([r,c-1])
            if c < C-1 and not visited[r][c+1]:
                visited[r][c+1]=True
                queue.append([r,c+1])
                out.append([r,c+1])
            if r < R-1 and not visited[r+1][c]:
                visited[r+1][c]=True
                queue.append([r+1,c])
                out.append([r+1,c])
        return out

R = 2
C = 2
r0 = 0
c0 = 1
sl=Solution()
print(sl.allCellsDistOrder(R,C,r0,c0))
            
                
                
