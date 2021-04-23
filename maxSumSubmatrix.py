from typing import *

#TLE
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        presum=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                presum[i+1][j+1]=presum[i][j+1]+presum[i+1][j]-presum[i][j]+matrix[i][j]
        
        out=-123456789
        # print(presum)
        for i1 in range(len(matrix)):
            for i2 in range(i1,len(matrix)):
                for j1 in range(len(matrix[0])):
                    for j2 in range(j1,len(matrix[0])):
                        tmp=presum[i2+1][j2+1]+presum[i1][j1]-presum[i1][j2+1]-presum[i2+1][j1]
                        if tmp<=k:
                            out=max(tmp,out)
                            if out==k:
                                return out
        return out

sl=Solution()
matrix = [[2,2,-1]]
k = 3
print(sl.maxSumSubmatrix(matrix,k))
                            
                
