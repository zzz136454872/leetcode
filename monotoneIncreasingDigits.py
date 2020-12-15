from typing import *

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums=[int(i) for i in list(str(N))]
        i=0
        while i<len(nums)-1 and nums[i]<=nums[i+1]:
            i+=1
        if i==len(nums)-1:
            return N
        j=i
        while j>0 and nums[j-1]==nums[i]:
            j-=1
        nums[j]-=1
        for i in range(j+1,len(nums)):
            nums[i]=9
        return int(''.join([str(i) for i in nums]))

sl=Solution()
inp=1234
print(sl.monotoneIncreasingDigits(inp))
