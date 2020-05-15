from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        log={0:1}
        count=0
        
        for num in nums:
            prefix+=num
            if prefix-k in log.keys():
                count+=log[prefix-k]
            log[prefix]=log[prefix]+1 if prefix in log.keys() else 1
        return count
sl=Solution()
nums = [1,1,1]
k=2
print(sl.subarraySum(nums,k))
                
