from typing import *

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        log=[0 for i in range(len(nums))]
        log[0]=nums[0]
        stack=[nums[0]]
        for i in range(1,len(nums)):
            prev=i-k-1
            if prev>=0 and stack[0]==log[prev]:
                stack.pop(0)
            # print(stack)
            log[i]=stack[0]+nums[i]
            while len(stack)>0 and stack[-1]<log[i]:
                stack.pop()
            stack.append(log[i])
            # print(stack,log,prev)
        # print(log)
        return log[-1]

sl=Solution()
nums=[100,-1,-100,-1,100]
k=2
print(sl.maxResult(nums,k))
