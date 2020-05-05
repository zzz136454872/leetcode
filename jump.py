from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        count=[30000 for i in range(len(nums))]
        count[0]=0
        for i in range(len(nums)):
            if i>0 and nums[i]<nums[i-1]:
                continue
            print('flag',i,nums[i])
            for j in range(i+1,nums[i]+i+1):
                if j>=len(nums):
                    break
                if count[i]+1<count[j]:
                    count[j]=count[i]+1
            #print(count)
        return count[-1]

inp=[25000,24999,24998,24997,24996,24995,24994,24993,24992,24991,24990,24989,24988,24987,24986,24985,24984,24983,24982,24981,24980,24979,24978,24977,24976,24975,24974,24973,24972,24971,24970,24969,24968,24967,24966,24965,24964,24963,24962,24961,24960,24959,24958,24957,24956,24955,24954,24953,24952,24951]
sl=Solution()
print(sl.jump(inp))

