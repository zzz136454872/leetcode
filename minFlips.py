from typing import *
import copy

def c(a):
    return 1 if a==0 else 0

def change(mat, y, x):
    mat[y][x]=c(mat[y][x])
    if y>0:
        mat[y-1][x]=c(mat[y-1][x])
    if x>0:
        mat[y][x-1]=c(mat[y][x-1])
    if y<len(mat)-1:
        mat[y+1][x]=c(mat[y+1][x])
    if x<len(mat[0])-1:
        mat[y][x+1]=c(mat[y][x+1])

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        if len(mat)<len(mat[0]):#转置
            mat=[[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
        min_change=10000
        for i in range(2**len(mat[0])):
            a=bin(i)[2:]
            a=(len(mat[0])-len(a))*'0'+a
            now_change=0
            mat1=copy.deepcopy(mat)
            for j in range(len(a)):
                if a[j]=='0':
                    continue
                change(mat1,0,j)
                now_change+=1
            for k in range(1,len(mat)):
                for j in range(0,len(a)):
                    if mat1[k-1][j]==1:
                        change(mat1,k,j)
                        now_change+=1
            if not 1 in mat1[-1]:
                min_change=min(min_change,now_change)
        if min_change==10000:
            return -1
        return min_change

sl=Solution()
mat = [[1,1,1],[1,0,1],[0,0,0]]
#change(mat, 0, 1)
#print(mat)
print(sl.minFlips(mat))
                    
            
