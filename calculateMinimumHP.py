from typing import *

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        log=[12345 for i in range(len(dungeon[0])+1)]
        log[-1]=1
        log[-2]=1
        for i in range(len(dungeon)-1,-1,-1):
            if i!=len(dungeon)-1:
                log[-1]=12345
            for j in range(len(dungeon[0])-1,-1,-1):
                log[j]=max(min(log[j],log[j+1])-dungeon[i][j],1)
            print(log)
        return log[0]

sl=Solution()

inp=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(sl.calculateMinimumHP(inp))

