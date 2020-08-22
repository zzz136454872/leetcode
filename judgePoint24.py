from typing import *

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                tmp=[nums[i]+nums[j],nums[i]-nums[j],nums[j]-nums[i],nums[i]*nums[j]]
                if  nums[j]!=0:
                    tmp.append(nums[i]/nums[j])
                if nums[i]!=0:
                    tmp.append(nums[j]/nums[i])
                if len(nums)==2:
                    for num in tmp:
                        if abs(num-24)<0.000001:
                            return True
                    return False
                nums1=nums.copy()
                del nums1[j]
                del nums1[i]
                for n in tmp:
                    if self.judgePoint24(nums1+[n]):
                        return True
        return False

    
nums=[3,3,8,8]
sl=Solution()
print(sl.judgePoint24(nums))
