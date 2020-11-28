from typing import *

# 逆序对计数
class Solution1:
    def reversePairs(self, nums: List[int]) -> int:
        log=[]
        out=0
        for num in nums:
            start=0
            end=len(log)-1
            while start<=end:
                mid=(start+end)//2
                if log[mid]>num:
                    start=mid+1
                else:
                    end=mid-1
            out+=start
            log.insert(start,num)
        return out

# 翻转对
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeCount(start,end):
            if start>=end:
                return 0
            out=0
            mid=(start+end)//2
            out=mergeCount(start,mid)
            out+=mergeCount(mid+1,end)
            i=start
            j=mid+1
            while i<=mid:
                while j<=end and 2*nums[j]<nums[i]:
                    j+=1
                out+=j-mid-1
                i+=1
            sub1=nums[start:mid+1]
            sub2=nums[mid+1:end+1]
            i=0
            j=0
            k=start
            while i<len(sub1) and j<len(sub2):
                if sub1[i]<sub2[j]:
                    nums[k]=sub1[i]
                    i+=1
                else:
                    nums[k]=sub2[j]
                    j+=1
                k+=1
            while i<len(sub1):
                nums[k]=sub1[i]
                i+=1
                k+=1
            while j<len(sub2):
                nums[k]=sub2[j]
                j+=1
                k+=1
            # print(start,end,out,nums[start,end+1])
            return out
        return mergeCount(0,len(nums)-1)

inp=[2,4,3,5,1]
inp=[1,3,2,3,1]
sl=Solution()
print(sl.reversePairs(inp))

