from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        import copy
        tmp=copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[j][len(matrix[0])-1-i]=tmp[i][j]
                print(i,j,tmp[i][j])

inp=[[1,2,3],
  [4,5,6],
  [7,8,9]
]

sl=Solution()
print(sl.rotate(inp))
print(inp)



