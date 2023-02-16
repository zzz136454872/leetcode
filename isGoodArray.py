from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)

        for i in range(1,len(nums)):
            nums[0]=gcd(nums[0],nums[i])
        return nums[0]==1
