from typing import *

class Solution:
    def update(self):
        while len(self.queue)>0:
            i=self.queue[0][0]
            j=self.queue[0][1]
            del(self.queue[0])
            if i>0:
                if self.matrix[i-1][j]>self.matrix[i][j]+1:
                    self.matrix[i-1][j]=self.matrix[i][j]+1
                    self.queue.append((i-1,j))
            if j>0:
                if self.matrix[i][j-1]>self.matrix[i][j]+1:
                    self.matrix[i][j-1]=self.matrix[i][j]+1
                    self.queue.append((i,j-1))
            if i<len(self.matrix)-1:
                if self.matrix[i+1][j]>self.matrix[i][j]+1:
                    self.matrix[i+1][j]=self.matrix[i][j]+1
                    self.queue.append((i+1,j))
            if j<len(self.matrix[0])-1:
                if self.matrix[i][j+1]>self.matrix[i][j]+1:
                    self.matrix[i][j+1]=self.matrix[i][j]+1
                    self.queue.append((i,j+1))

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        self.matrix=matrix
        self.queue=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.matrix[i][j]!=0 \
                    and not(i>0 and self.matrix[i-1][j]==0)\
                    and not(j>0 and self.matrix[i][j-1]==0)\
                    and not(i<len(self.matrix)-1 and self.matrix[i+1][j]==0)\
                    and not(j<len(self.matrix[0])-1 and self.matrix[i][j+1]==0):
                    self.matrix[i][j]=1000;
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(self.matrix[i][j]==1):
                    self.queue.append((i,j))
                    self.update()
        return self.matrix

sl=Solution()
print(sl.updateMatrix(inp))
