from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        longest=0

        for num in ns:
            if num-1 not in ns:
                now=num
                now_length=1
                while now+1 in ns:
                    now+=1
                    now_length+=1
                longest=max(longest,now_length)
        return longest

nums=[100, 4, 200, 1, 3, 2]
sl=Solution()
print(sl.longestConsecutive(nums))
        
