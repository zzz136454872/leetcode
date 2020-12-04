from typing import *

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        s1=0
        s2=0
        s3=0
        previous=-1
        i=0
        while i<len(nums):
            now=nums[i]
            starti=i
            while i<len(nums) and now==nums[i]:
                i+=1
            count=i-starti
            if(now-previous>1):
                if(s1!=0 or s2!=0):
                        return False
                s1=count
                s2=0
                s3=0
                previous=now
                continue
            previous=now
            if count<s1+s2 :
                return False
            rest=count-s1-s2
            keep=min(rest, s3)
            s3=keep+s2;
            s2=s1
            s1=rest-keep
            # print(i,now,count,s1,s2,s3)
        return s1==0 and s2==0

sl=Solution()
inp=[1,2,3,3,4,4,5,5]
print(sl.isPossible(inp))
