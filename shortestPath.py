from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        if k>=m+n-3:
            return m+n-2
        mem=[]

        def find(m,r,c):
        
        return find(k,m-1,n-1)
