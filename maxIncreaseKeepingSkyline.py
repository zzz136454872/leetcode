from typing import *


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        heriMax=[]
        vertMax=[]
        for i in range(len(grid)):
            heriMax.append(max(grid[i]))
        for j in range(len(grid[0])):
            tmp=grid[0][j]
            for i in range(len(grid)):
                tmp=max(tmp,grid[i][j])
            vertMax.append(tmp)
        out=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                out+=(min(heriMax[i],vertMax[j])-grid[i][j])
        return out
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
sl=Solution()
print(sl.maxIncreaseKeepingSkyline(grid))

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# aa=zip(a,b)
# print(list(aa))
# aaa=zip(a,b,c)
# print(list(zip(*aaa)))


