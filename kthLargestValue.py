from typing import *

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        log=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                log[i+1][j+1]=matrix[i][j]^log[i][j]^log[i+1][j]^log[i][j+1]
        log=[log[i][j] for i in range(1,len(matrix)+1) for j in range(1,len(matrix[0])+1)]
        return sorted(log,reverse=True)[k-1]
        # return kLargest(log,k)

sl=Solution()
matrix = [[5,2],[1,6]]
k = 3
matrix=[[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]]
k=2
print(sl.kthLargestValue(matrix,k))

