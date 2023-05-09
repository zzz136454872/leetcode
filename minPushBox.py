from typing import List
from functools import cache


# WA
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        tx=0
        ty=0
        sbx=0
        sby=0
        srx=0
        sry=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='B':
                    sbx=i
                    sby=j
                elif grid[i][j]=='T':
                    tx=i
                    ty=j
                elif grid[i][j]=='S':
                    srx=i
                    sry=j
        BIG=123456
        visiting=set()
        
        @cache
        def find(xb,yb,xh,yh):
            # print('inside',xb,yb,xh,yh)
            if (xb,yb,xh,yh) in visiting:
                return BIG
            visiting.add((xb,yb,xh,yh))
            if xb<0 or xb>=m or xh<0 or xh>=m:
                visiting.discard((xb,yb,xh,yh))
                return BIG
            if yb<0 or yb>=n or yh<0 or yh>=n:
                visiting.discard((xb,yb,xh,yh))
                return BIG
            if grid[xb][yb]=='#' or grid[xh][yh]=='#':
                visiting.discard((xb,yb,xh,yh))
                return BIG
            if xb==xh and yb==yh or tx==xh and ty==yh:
                visiting.discard((xb,yb,xh,yh))
                return BIG
            if xb==tx and yb==ty:
                visiting.discard((xb,yb,xh,yh))
                return 0
            res=BIG
            if xb!=xh-1 or yb!=yh:
                res=min(res,find(xb,yb,xh-1,yh))
            else:
                res=min(res,1+find(xb-1,yb,xh-1,yh))
            if xb!=xh+1 or yb!=yh:
                res=min(res,find(xb,yb,xh+1,yh))
            else:
                res=min(res,1+find(xb+1,yb,xh+1,yh))
            if yb!=yh-1 or xb!=xh:
                res=min(res,find(xb,yb,xh,yh-1))
            else:
                res=min(res,1+find(xb,yb-1,xh,yh-1))
            if yb!=yh+1 or xb!=xh:
                res=min(res,find(xb,yb,xh,yh+1))
            else:
                res=min(res,1+find(xb,yb+1,xh,yh+1))
            visiting.discard((xb,yb,xh,yh))
            if res<BIG:
                print(xb,yb,xh,yh,res)
            return res

        r=find(sbx,sby,srx,sry)
        return r if r<BIG else -1

grid = [["#","#","#","#","#","#"],
         ["#","T","#","#","#","#"],
         ["#",".",".","B",".","#"],
         ["#",".","#","#",".","#"],
         ["#",".",".",".","S","#"],
         ["#","#","#","#","#","#"]]

grid = [["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#","#","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

grid = [["#","#","#","#","#","#"],
        ["#","T",".",".","#","#"],
        ["#",".","#","B",".","#"],
        ["#",".",".",".",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

grid= [["#",".",".","#","#","#","#","#"],
       ["#",".",".","T","#",".",".","#"],
       ["#",".",".",".","#","B",".","#"],
       ["#",".",".",".",".",".",".","#"],
       ["#",".",".",".","#",".","S","#"],
       ["#",".",".","#","#","#","#","#"]]

grid = [["#","#",".","#",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".","T",".","#"],
        [".",".",".",".",".","#",".","."],
        [".",".",".",".",".","#",".","."],
        [".",".",".",".",".",".","S","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".",".",".",".",".","."]]

# ##.#....
# ........
# .....T.#
# .....#..
# .....#..
# ......S.
# ...B....
# ........

print(Solution().minPushBox(grid))

                
            
