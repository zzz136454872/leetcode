from typing import *

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start=0
        end=len(A)-1
        while start<=end:
            mid=(start+end)//2
            if A[mid]>=0:
                end=mid-1
            else:
                start=mid+1
        p=start-1
        q=start
        out=[]
        while p>=0 and q<len(A):
            if abs(A[p])<abs(A[q]):
                out.append(A[p]**2)
                p-=1
            else:
                out.append(A[q]**2)
                q+=1
        while p>=0:
            out.append(A[p]**2)
            p-=1
        while q<len(A):
            out.append(A[q]**2)
            q+=1
        return out

sl=Solution()
A=[-7,-3,2,3,11]
print(sl.sortedSquares(A))
            

                
                
        
