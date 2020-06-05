from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        log=[[True for j in range(len(matrix[0]))] for i in range(len(matrix))]
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        direction=0
        change=0
        i=0
        j=0
        out=[matrix[0][0]]
        log[0][0]=False
        while(True):
            if direction==0:
                if j<len(matrix[0])-1 and log[i][j+1]:
                    j+=1
                    log[i][j]=False
                    out.append(matrix[i][j])
                    change=0
                else:
                    if change>=2:
                        break
                    change+=1
                    direction=1
            elif direction==1:
                if i<len(matrix)-1 and log[i+1][j]:
                    i+=1
                    log[i][j]=False
                    out.append(matrix[i][j])
                    change=0
                else:
                    if change>=2:
                        break
                    change+=1
                    direction=2
            elif direction==2:
                if j>0 and log[i][j-1]:
                    j-=1
                    log[i][j]=False
                    out.append(matrix[i][j])
                    change=0
                else:
                    if change>=2:
                        break
                    change+=1
                    direction=3
            elif direction==3:
                if i>0 and log[i-1][j]:
                    i-=1
                    log[i][j]=False
                    out.append(matrix[i][j])
                    change=0
                else:
                    if change>=2:
                        break
                    change+=1
                    direction=0
        return out

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sl=Solution()
print(sl.spiralOrder(matrix))

