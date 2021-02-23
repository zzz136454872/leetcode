from typing import *

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        out=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                out+=customers[i]
                customers[i]=0
        madd=sum(customers[:X])
        now=madd
        for i in range(len(customers)-X):
            now+=customers[i+X]-customers[i]
            madd=max(now,madd)
        out+=madd
        return out

sl=Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(sl.maxSatisfied(customers,grumpy,X))



