from typing import *

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        out=0
        self.grid=grid

        for i in range(len(grid)-2):
            for j in range(len(grid[0]-2)):
                if grid[i+1][j+1]!=5:
                    continue
                else:
                    if self.check(i,j) :
                        out+=1
        return out

    def check(self,x,y):
        log=[False for i in range(11)]
        for i in range(x,x+3):
            for j in range(y,y+3):
                log[i]=True
                



