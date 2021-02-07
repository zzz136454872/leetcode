from typing import *

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for j in range(n):
            now=0
            for i in range(m-1,-1,-1):
                if matrix[i][j]==0:
                    now=0
                else:
                    now+=1
                    matrix[i][j]=now

        out=0
        # print(matrix)
        for i in range(m):
            tmp=sorted([matrix[i][j] for j in range(n)],reverse=True)
            for j in range(n):
                out=max(out,tmp[j]*(j+1))
                if tmp[j]==0:
                    break

        return out

sl=Solution()
matrix=[[0,0,1],[1,1,1],[1,0,1]]
print(sl.largestSubmatrix(matrix))

                
