from typing import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return 0
        tmp=0
        log=[]
        for num in nums:
            if num%2==0:
                tmp+=1
            else:
                log.append(tmp)
                tmp=0
        log.append(tmp)
        out = 0
        for i in range(len(log)-k):
            out+=(log[i]+1)*(1+log[i+k])
        return out

sl=Solution()
nums=[2,2,2,1,2,2,1,2,2,2]
k=2
print(sl.numberOfSubarrays(nums,k))

            

