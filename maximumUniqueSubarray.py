from typing import *

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        log=[0 for i in range(10001)]
        outCount=0
        out=0
        r=0
        s=0
        for i in range(len(nums)):
            while outCount==0:
                out=max(out,s)
                if r<len(nums):
                    s+=nums[r]
                    log[nums[r]]+=1
                    if log[nums[r]]>1:
                        outCount+=1
                    r+=1
                else:
                    return out

            s-=nums[i]
            # print(s)
            log[nums[i]]-=1
            if log[nums[i]]==1:
                outCount-=1
        return out

sl=Solution()
nums=[10000]
print(sl.maximumUniqueSubarray(nums))
            
        

