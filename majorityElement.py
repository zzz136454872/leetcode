from typing import *

# 求众数1
class Solution1:
    def majorityElement(self, nums) :
        log=dict()
        for num in nums:
            if num in log.keys():
                log[num]+=1
            else:
                log[num]=0
        for key in log.keys():
            if log[key]>=len(nums)/2:
                return key
        return 0

#求众数2
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        major=[]
        count=[]
        for num in nums:
            find=False
            for i in range(len(major)):
                if num==major[i]:
                    count[i]+=1
                    find=True
            if find:
                continue
            if len(major)<2:
                count.append(1)
                major.append(num)
                continue
            count[1]-=1
            if count[1]==0:
                del count[1]
                del major[1]
            count[0]-=1
            if count[0]==0:
                del count[0]
                del major[0]
        out=[]
        for num in major:
            if nums.count(num)>len(nums)//3:
                out.append(num)
        return out

sl=Solution()

inp=[1,1,1,3,3,2,2,2]
print(sl.majorityElement(inp))

        
