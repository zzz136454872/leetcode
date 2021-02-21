from typing import *

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)<=1:
            return len(nums)
        min_stack=[nums[0]]
        max_stack=[nums[0]]
        
        out=0
        end=1
        for start in range(len(nums)):
            while max_stack[0]-min_stack[0]<=limit:
                out=max(out,end-start)
                if end<len(nums):
                    while len(max_stack)>0 and max_stack[-1]<nums[end]:
                        max_stack.pop()
                    max_stack.append(nums[end])
                    while len(min_stack)>0 and min_stack[-1]>nums[end]:
                        min_stack.pop()
                    min_stack.append(nums[end])
                    end+=1
                else:
                    break
            if min_stack[0]==nums[start]:
                min_stack.pop(0)
            if max_stack[0]==nums[start]:
                max_stack.pop(0)
        return out

nums = [10,1,2,4,7,2]
limit = 5
sl=Solution()
print(sl.longestSubarray(nums,limit))

