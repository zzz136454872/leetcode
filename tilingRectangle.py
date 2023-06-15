from typing import List


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        mem=[[False]*m for i in range(n)]
        r=max(m,n)
    
        def find():
            res=r
            up=False
            for i in range(n):
                for j in range(m):
                    if not mem[i][j]:
                        up=True
                        for k in range(1,r+1):
                            if not able(i,j,k):
                                break
                            # print('i',i,'j',j,'k',k,'r',r)
                            change(i,j,k,True)
                            res=min(res,1+find())
                            change(i,j,k,False)
            if not up:
                return 0
            return res
        
        def able(i,j,k):
            if i+k>n or j+k>m:
                return False
            for ii in range(k):
                for jj in range(k):
                    if mem[i+ii][j+jj]:
                        return False
            return True

        def change(i,j,k,c):
            for ii in range(k):
                for jj in range(k):
                    mem[i+ii][j+jj]=c
        return find()

n = 2
m = 3
n = 3
m = 3
print(Solution().tilingRectangle(n,m))

            
