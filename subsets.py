from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        out=[]
        for i in range(2**n):
            tmpSet=[]
            tmp=bin(i)[2:]
            tmp=(n-len(tmp))*'0'+tmp
            for j in range(n):
                if tmp[j]=='1':
                    tmpSet.append(nums[j])
            out.append(tmpSet)
        return out

nums=[1,2,3]
sl=Solution()
print(sl.subsets(nums))
