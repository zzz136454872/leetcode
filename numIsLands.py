from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid=grid
        count=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j]=='1':
                    count+=1
                    self.erase(i,j)
        return count

    def erase(self,i:int,j:int) -> None:
        if self.grid[i][j]!='0':
            return 
        self.grid[i][j]='0'
        if i>0:
            self.erase(i-1,j)
        if j>0:
            self.erase(i,j-1)
        if i<len(self.grid)-1:
            self.erase(i+1,j)
        if j<len(self.grid[0])-1:
            self.erase(i,j+1)
sl=Solution()
inp=[[1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]]

print(sl.numIslands(inp))

