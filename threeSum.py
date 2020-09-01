from typing import *

# a TLE solution
class Solution0:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        table=set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if (nums[i],nums[j]) in table:
                    continue
                else:
                    table.add((nums[i],nums[j]))
                target=-nums[i]-nums[j]
                start=j+1
                end=len(nums)-1
                while start<=end:
                    mid=(start+end)//2
                    if nums[mid]==target:
                        out.append([nums[i],nums[j],nums[mid]])
                        break
                    elif nums[mid]>target:
                        end=mid-1
                    else:
                        start=mid+1
        return out

# double pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    out.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        return out

nums= [-1,0,1,2,-1,-4]
sl=Solution()
print(sl.threeSum(nums))

