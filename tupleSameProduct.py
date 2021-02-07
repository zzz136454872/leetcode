from typing import *

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        log={}
        for i in range(n-1):
            for j in range(i+1,n):
                p=nums[i]*nums[j]
                if p not in log.keys():
                    log[p]=1
                else:
                    log[p]+=1
        out=0
        print(log)
        for c in log.values():
            out+=(c-1)*c//2
        return out*8

sl=Solution()
nums = [2,3,4,6,8,12]
print(sl.tupleSameProduct(nums))

            
