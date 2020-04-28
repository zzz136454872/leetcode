from typing import *

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        log = [0 for i in range(10005)]
        for num in nums:
            log[num]+=1
        out=[]
        for i in range(len(log)):
            if log[i]==1:
                out.append(i)
        return out

inp=[1,2,10,4,1,4,3,3]
sl=Solution()
print(sl.singleNumbers(inp))
