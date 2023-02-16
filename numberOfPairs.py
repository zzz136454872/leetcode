from typing import List
from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mem=defaultdict(int)
        for num in nums:
            mem[num]+=1
        res=[0,0]
        for v in mem.values():
            res[0]+=v//2
            res[1]+=v%2
        return res

nums = [1,3,2,1,3,2,2]
print(Solution().numberOfPairs(nums))

                
