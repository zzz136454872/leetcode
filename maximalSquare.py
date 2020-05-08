from typing import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        log=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    if i > 0 and j > 0:
                        log[i][j]=min(log[i-1][j],log[i][j-1],log[i-1][j-1])+1
                    else:
                        log[i][j]=1
                    if log[i][j] > m:
                        m=log[i][j]
        return m**2
                    
sl=Solution()

inp=[['1','0','1','0','0'],
     ['1','0','1','1','1'],
     ['1','1','1','1','1'],
     ['1','0','0','1','0']]
print(sl.maximalSquare(inp))
