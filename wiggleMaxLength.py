from typing import *

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        preDiff=0
        count=1
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            if preDiff>=0 and diff<0 or preDiff<=0 and diff>0:
                count+=1
                preDiff=diff
        return count

sl=Solution()
inp=[1,7,4,9,2,5]
print(sl.wiggleMaxLength(inp))
        
