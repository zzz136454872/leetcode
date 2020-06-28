from typing import *

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        start=0
        nums=numbers
        end=len(nums)-1
        if nums[start] < nums[end]:
            return nums[0]
        while start<end-1:
            mid=(start+end)//2
            print(start,mid,end)
            if nums[mid]<nums[end]:
                end=mid
            elif nums[mid]>nums[end]:
                start=mid
            else:
                start+=1
        return nums[end]

sl=Solution()
inp=[2,1,2,2,2]
print(sl.minArray(inp))
                


