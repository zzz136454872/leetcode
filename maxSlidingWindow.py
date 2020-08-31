from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0:
            return []
        queue=[]
        def push(num):
            while len(queue)>0 and queue[-1]<nums[i]:
                queue.pop()
            queue.append(num)
        for i in range(k):
            push(nums[i])
        out=[]
        out.append(queue[0])
        for i in range(k,len(nums)):
            j=i-k
            if nums[j]==queue[0]:
                del queue[0]
            push(nums[i])
            out.append(queue[0])
        return out

nums = [8,3,-1,-3,5,3,6,7]
k = 3
sl=Solution()
print(sl.maxSlidingWindow(nums,k))
        
