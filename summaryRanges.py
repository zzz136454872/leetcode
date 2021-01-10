from typing import *

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out=[]
        if len(nums)==0:
            return out
        pre=nums[0]
        pre_start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=pre+1:
                if pre_start==pre:
                    out.append(str(pre))
                else:
                    out.append(str(pre_start)+'->'+str(pre))
                pre_start=nums[i]
            pre=nums[i]

        if pre_start==pre:
            out.append(str(pre))
        else:
            out.append(str(pre_start)+'->'+str(pre))
            
        return out
            

nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
sl=Solution()
print(sl.summaryRanges(nums))
