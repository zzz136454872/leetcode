from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        log=0
        for num in nums:
            tmp=1<<(num-1)
            if(tmp&log):
                return num
            log=log|tmp
inp=[3,1,3,4,2]
sl=Solution()
print(sl.findDuplicate(inp))
