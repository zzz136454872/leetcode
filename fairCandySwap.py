from typing import *

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        B.sort()
        target=sum(A)-sum(B)
        target=target//2
        j=0
        for i in range(len(A)):
            want=A[i]-target
            while j<len(B)-1 and B[j]<want:
                j+=1
            if B[j]==want:
                return [A[i],B[j]]

        return [0,0] # not here


sl=Solution()
A = [1,2,5]
B = [2,4]
print(sl.fairCandySwap(A,B))
                
            


        
