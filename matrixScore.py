from typing import *
import copy

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if len(A)==0 or len(A[0])==0:
            return 0
        def sub(A):
            for i in range(len(A)):
                if A[i][0]==0:
                    for j in range(len(A[0])):
                        A[i][j]=1 if A[i][j]==0 else 0
            out=(1<<(len(A[0])-1))*len(A)
            for j in range(1,len(A[0])):
                count=0
                for i in range(len(A)):
                    if A[i][j]:
                        count+=1
                out+=max(count,len(A)-count)*(1<<(len(A[0])-1-j))
            return out
        out=sub(copy.deepcopy(A))
        for i in range(len(A)):
            A[i][0]=1 if A[i][0]==0 else 0
        return max(out,sub(A))
sl=Solution()
inp=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(sl.matrixScore(inp))
