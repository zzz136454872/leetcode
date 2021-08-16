from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        j=len(nums)-1
        out=[]
        while i<=j:
            out.append(nums[i])
            i+=1
            if i<=j:
                out.append(nums[j])
                j-=1
        return out


sl=Solution()
nums = [1,2,3,4,5]
print(sl.rearrangeArray(nums))

