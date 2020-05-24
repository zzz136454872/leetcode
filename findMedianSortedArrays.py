from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        mid=len(nums)//2
        if len(nums)!=2*mid:
            return nums[mid]
        else:
            return (nums[mid-1]+nums[mid])/2


nums1 = [1, 2]
nums2 = [3, 4]
sl=Solution()
print(sl.findMedianSortedArrays(nums1,nums2))
