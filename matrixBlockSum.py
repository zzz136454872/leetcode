from typing import *

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mid=[[0 for j in range(len(mat[0]))] for j in range(len(mat))]
        out=[[0 for j in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            tmp=0
            for j in range(min(K,len(mat[0]))):
                tmp+=mat[i][j]
            #print(tmp)
            for j in range(len(mat[0])):
                if j+K<len(mat[0]):
                    tmp+=mat[i][j+K]
                if j>K:
                    tmp-=mat[i][j-K-1]
                mid[i][j]=tmp
        #print(mid)
        for j in range(len(mat[0])):
            tmp=0
            for i in range(min(K,len(mat))):
                tmp+=mid[i][j]
            for i in range(len(mat)):
                if i+K<len(mat):
                    tmp+=mid[i+K][j]
                if i>K:
                    tmp-=mid[i-K-1][j]
                out[i][j]=tmp
        return out

sl=Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
print(sl.matrixBlockSum(mat,K))
