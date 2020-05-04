from typing import *

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.matrix=martix
        maximal=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i]=="1":
                    tmp=max(maximal,seek(i,j)) 
                    area=tmp[0]*tmp[1]
                    maximal=max(maximal,area)

    def seek(self,i,j):
        if i>len(self.matrix) or j>len(self.matrix[0]) or self.matrix[i][j]=='0':
            return (0,0)
        else:
            right=min(seek(i,j+1)[0],seek(i+1,j)[0]+1)
            down=min(seek(i,j+1)[1]+1,seek(i+1,j)[1])
            return (right,down)

           

                


