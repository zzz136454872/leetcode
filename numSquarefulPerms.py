from typing import *
import math

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        print(A)
        visited=[False for i in A]

        def isSquare(n):
            return int(math.sqrt(n))**2==n

        def dfs(k,last):
            #print(k,last,visited)
            if k==len(A):
                #print('get 1')
                return 1
            out=0
            i=0

            pre_test=-1
            if k==0:
                while i<len(A):
                    visited[i]=True
                    out+=dfs(1,A[i])
                    visited[i]=False
                    pre_test=i
                    i+=1
                    while i<len(A) and A[i]==A[pre_test]:
                        i+=1
                return out

            while i<len(A):
                #print(i,visited)
                if not visited[i] and isSquare(A[i]+last):
                    #print('inside',i,pre_test)
                    visited[i]=True
                    out+=dfs(k+1,A[i])
                    visited[i]=False
                    pre_test=i
                i+=1
                while i<len(A) and pre_test!=-1 and A[i]==A[pre_test]:
                    i+=1
                #print('go next',i)
            return out

        return dfs(0,0)

sl=Solution()
inp=[2,2,2]
print(sl.numSquarefulPerms(inp))

