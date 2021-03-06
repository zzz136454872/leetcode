from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        out=[-1 for i in nums]
        for i in range(len(nums)-1,-1,-1):
            while len(stack)>0 and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)>0:
                out[i]=stack[-1]
            stack.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while len(stack)>0 and stack[-1]<=nums[i]:
                stack.pop()
            if out[i]==-1 and len(stack)>0:
                out[i]=stack[-1]
            stack.append(nums[i])
        return out

sl=Solution()
inp=[1,2,1]
print(sl.nextGreaterElements(inp))
            
