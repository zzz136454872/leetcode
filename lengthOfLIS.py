# one solution
# class Solution:
#     def lengthOfLIS(self, nums):
#         log=[0 for i in range(len(nums))]
#         for i in range(len(nums)):
#             m=0
#             for j in range(i):
#                 if nums[j]<nums[i]:
#                     m=max(m,log[j])
#                 log[i]=m+1
#         return max(log)
#


# another solution
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        log = []

        for num in nums:
            if len(log) == 0 or num > log[-1]:
                log.append(num)

                continue
            start = 0
            end = len(log) - 1

            while start <= end:
                mid = (start + end) // 2

                if log[mid] >= num:
                    end = mid - 1
                else:
                    start = mid + 1
            log[start] = num

        return len(log)


sl = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(sl.lengthOfLIS(nums))
