from typing import List


# wa
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        def test(x,y):
            if x<0 or x>=n or y<0 or y>=m:
                return False
            
            if grid[x][y]==1 or grid[x][y]==2:
                return True
            grid[x][y]=2
            return test(x+1,y) and test(x-1,y) and test(x,y+1) and test(x,y-1)
            
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and test(i,j):
                    res+=1
        return res

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

print(Solution().closedIsland(grid))
