from typing import *

# not finished
class Solution:
    def getK(self, nums: str, k: int) -> str:
        if k==0:
            return []
        if len(nums)-k==0:
            return nums.copy()
        stack=[]
        for i in range(len(nums)):
            # print(stack)
            while len(stack)>0 and nums[i]>stack[-1] and len(nums)-i+len(stack)>k:
                stack.pop()
            stack.append(nums[i])
        stack=stack[:k]
        return stack
    
    def merge(self,a,b):
        out=[]
        while a or b:
            bigger=a if a>b else b
            out.append(bigger.pop(0))
        return out

    def cmp(self,a,b):
        # print(a,b)
        if len(a)!=len(b):
            return len(a)-len(b)
        for i in range(len(a)):
            if a[i]!=b[i]:
                return a[i]-b[i]
        return 0

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        outValue=[]
        for i in range(k+1):
            if i<=len(nums1) and k-i<=len(nums2):
                # print(i,k-i,self.getK(nums1,i),self.getK(nums2,k-i))
                nowValue=self.merge(self.getK(nums1,i),self.getK(nums2,k-i))
                if self.cmp(outValue,nowValue)<0:
                    outValue=nowValue
        return outValue

sl=Solution()
nums1= [6,6,8]
nums2= [5,0,9]
k=3
print(sl.maxNumber(nums1,nums2,k))
# print(sl.getK(nums1,2))
# print(sl.merge(nums1,nums2))

