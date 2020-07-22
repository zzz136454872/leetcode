from typing import *

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        start=0
        nums=numbers
        end=len(nums)-1
        if nums[start] < nums[end]:
            return nums[0]
        while start<end:
            mid=(start+end)//2
            #print(start,mid,end)
            if nums[mid]>nums[end]:
                start=mid+1
            elif nums[mid]<nums[end]:
                end=mid
            else:
                end-=1
        return nums[start]

sl=Solution()
inp=[2,1,2,2,2]
print(sl.minArray(inp))
                


