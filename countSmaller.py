from typing import *

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        log=[]
        out=[]
        for i in range(len(nums)-1,-1,-1):
            left=0
            right=len(log)-1
            while left <= right:
                mid=(left+right)//2
                if nums[i]<=log[mid]:
                    left=mid+1
                else:
                    right=mid-1
            out.insert(0,len(log)-left)
            log.insert(left,nums[i])
        return out

nums=[5,2,6,1]
sl=Solution()
print(sl.countSmaller(nums))

        
