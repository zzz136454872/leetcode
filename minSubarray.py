from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t=sum(nums)%p
        if t==0:
            return 0
        s=0
        mem={0:-1}
        res=len(nums)
        for i in range(len(nums)):
            s=(s+nums[i])%p
            if (s-t)%p in mem:
                print(i,s,t,(s-t)%p,mem)
                res=min(res,i-mem[(s-t)%p])
            mem[s]=i
        return res if res!=len(nums) else -1

nums = [3,1,4,2]
p = 6
nums = [6,3,5,2]
p = 9
nums = [1,2,3]
p = 3
nums = [1,2,3]
p = 7
print(Solution().minSubarray(nums,p))
            
            
