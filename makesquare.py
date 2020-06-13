from typing import *

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target==0:
            return False
        if target//4*4!=target:
            return False
        target=target//4
        for num in nums:
            if num > target:
                return False
        self.used=[False for i in range(len(nums))]
        nums.sort(reverse=True)
        self.nums=nums
        print(nums)
        for line in range(3):
            if not self.seek(0,target):
                return False
        return True

    def seek(self,index,num):
        #print(self.used)
        #print(self.nums,num)
        if num==0:
            return True
        for i in range(index,len(self.nums)):
            if not self.used[i] and num>=self.nums[i]:
                self.used[i]=True
                if self.seek(i,num-self.nums[i]):
                    return True
                self.used[i]=False
        return False
sl=Solution()
inp=[1,1,2,2,2]
print(sl.makesquare(inp))
                

            
        
        
