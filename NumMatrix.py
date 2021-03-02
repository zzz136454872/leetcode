from typing import *

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        if n==0:
            return 
        n0=len(matrix[0])
        pre_sum=[[0 for j in range(n0+1)] for i in range(n+1)]
        for i in range(n):
            tmp=0
            for j in range(n0):
                tmp+=matrix[i][j]
                pre_sum[i][j+1]=tmp

        #print(pre_sum)
        squ_sum=[[0 for j in range(n0+1)] for i in range(n+1)]
        # squ_sum[0]=pre_sum[0]
        for i in range(1,n+1):
            for j in range(1,n0+1):
                squ_sum[i][j]=squ_sum[i-1][j]+pre_sum[i-1][j]
        self.squ_sum=squ_sum
        #print(squ_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.squ_sum[row1][col1]+self.squ_sum[row2+1][col2+1]\
              -self.squ_sum[row1][col2+1]-self.squ_sum[row2+1][col1]
# Your NumMatrix object will be instantiated and called as such:
matrix = [ [3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5] ]
# matrix=[[1,2],[100,200]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))# -> 8
print(obj.sumRegion(1, 1, 2, 2))# -> 11
print(obj.sumRegion(1, 2, 2, 4))# -> 12

