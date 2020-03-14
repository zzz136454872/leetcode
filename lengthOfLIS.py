class Solution:
    def lengthOfLIS(self, nums):
        log=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            m=0
            for j in range(i):
                if nums[j]<nums[i]:
                    m=max(m,log[j])
                log[i]=m+1
        return max(log)
