from typing import *

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        out=0
        n0=len(matrix)
        n1=len(matrix[0])
        for i in range(n0):
            tmp=[0]*n1
            for j in range(i,n0):
                tmp=[tmp[k]+matrix[j][k] for k in range(n1)]
                prefix=0
                table={0:1}
                for num in tmp:
                    prefix+=num
                    out+=table.get(prefix-target,0)
                    table[prefix]=table.get(prefix,0)+1
        return out

sl=Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
matrix = [[1,-1],[-1,1]]
matrix = [[904]]
target = 0
print(sl.numSubmatrixSumTarget(matrix,target))
                    
                
            
                
