from typing import *

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        pre_min=[12345678901234 for i in range(len(nums))]
        stack=[(nums[0],0)]
        for i in range(1,len(nums)):
            pre_min[i]=min(pre_min[i-1],nums[i-1])
            while len(stack)>0 and stack[-1][0]<=nums[i]:
                stack.pop()
            if len(stack)>0:
                if pre_min[stack[-1][1]]<nums[i]:
                    return True
            stack.append((nums[i],i))
        return False

inp=[3,1,4,2]
sl=Solution()
print(sl.find132pattern(inp))


