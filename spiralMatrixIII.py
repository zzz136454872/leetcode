from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        turn = [cStart+1,rStart+1,cStart-1,rStart-1]
        dirs = 0
        res = []
        loc = [rStart,cStart]

        def end():
            return len(res)<rows*cols
                
        while end():
            if dirs==0:
                if loc[0]>=0:
                    for i in range(max(0,loc[1]),turn[0]):
                        res.append([loc[0],i])
                dirs=1
                loc[1]=turn[0]
                if turn[0]<cols:
                    turn[0]+=1

            elif dirs==1:
                if loc[1]<cols:
                    for i in range(max(0,loc[0]),turn[1]):
                        res.append([i,loc[1]])
                dirs=2
                loc[0]=turn[1]
                if turn[1]<rows:
                    turn[1]+=1

            elif dirs==2:
                if loc[0]<rows:
                    for i in range(min(loc[1],cols-1),turn[2],-1):
                        res.append([loc[0],i])
                dirs=3
                loc[1]=turn[2]
                if turn[2]>=0:
                    turn[2]-=1

            elif dirs==3:
                if loc[1]>=0:
                    for i in range(min(loc[0],rows-1),turn[3],-1):
                        res.append([i,loc[1]])
                dirs=0
                loc[0]=turn[3]
                if turn[3]>=0:
                    turn[3]-=1
        return res

rows = 1
cols = 4
rStart = 0
cStart = 0

rows = 5
cols = 6
rStart = 1
cStart = 4

print(Solution().spiralMatrixIII(rows,cols,rStart,cStart))
                        
