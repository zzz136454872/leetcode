from typing import *

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        out=0
        log={}
        for i in range(len(A)):
            for j in range(len(B)):
                tmp=A[i]+B[j]
                if tmp not in log.keys():
                    log[tmp]=1
                else:
                    log[tmp]+=1
        for i in range(len(C)):
            for j in range(len(D)):
                tmp=-C[i]-D[j]
                if tmp in log.keys():
                    out+=log[tmp]
        return out

sl=Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(sl.fourSumCount(A,B,C,D))
