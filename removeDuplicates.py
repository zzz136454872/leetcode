from typing import *

# 删除字符串中的所有相邻重复项
class Solution1:
    def removeDuplicates(self, S: str) -> str:
        out=''
        for letter in S:
            if len(out)==0:
                out+=letter
            else:
                if letter==out[-1]:
                    out=out[:-1]
                else:
                    out+=letter
        return out
sl=Solution1()
S="abbaca"
print(sl.removeDuplicates(S))

# 删除有序数组中的重复项 II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=0
        now=-123456
        count=0
        for q in range(len(nums)):
            if nums[q]!=now:
                count=1
                now=nums[q]
            else:
                count+=1

            if count<3:
                nums[p]=now
                p+=1
        del nums[p:]
        return p
sl=Solution()
nums = [1,1,1,2,2,3]
print(sl.removeDuplicates(nums))
print(nums)
            
