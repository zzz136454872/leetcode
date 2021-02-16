from typing import *

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start=max(nums)
        end=sum(nums)
        while start<end:
            mid=(start+end)//2
            count=1
            s=0
            for num in nums:
                s+=num
                if s>mid:
                    count+=1
                    s=num
            if count>m:
                start=mid+1
            else:
                end=mid
        return start


