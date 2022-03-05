from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            minStack=[nums[i]]
            maxStack=[nums[i]]
            for j in range(i+1,len(nums)):

