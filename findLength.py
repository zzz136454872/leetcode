from typing import *

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        max_len=0
        length=[[0 for j in range(len(A))] for i in range(len(B))]
        
        for i in range(len(B)):
            for j in range(len(A)):
                if B[i]==A[j]:
                    length[i][j]=1
                    if i > 0 and j>0:
                        length[i][j]+=length[i-1][j-1]
                    max_len=max(max_len,length[i][j])
        return max_len

sl=Solution()
A=[1,2,3,2,1]
B=[3,2,1,4,7]
print(sl.findLength(A,B))
