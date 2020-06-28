from typing import *

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        tmp=0
        front=0
        back=0
        min_len=len(nums)+1
        while True:
            if tmp<s:
                if front==len(nums):
                    break
                tmp+=nums[front]
                front+=1
            else:
                min_len=min(min_len,front-back)
                tmp-=nums[back]
                back+=1
        if min_len>len(nums):
            return 0
        else:
            return min_len
sl=Solution()
s = 7
nums = [2,3,1,2,4,3]
print(sl.minSubArrayLen(s,nums))
            


