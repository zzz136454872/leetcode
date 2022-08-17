from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums) / 2
        nums.sort(reverse=True)
        t = 0

        for i in range(len(nums)):
            t += nums[i]

            if t > s:
                nums = nums[:i + 1]

                break

        return nums


nums = [4, 3, 10, 9, 8]
nums = [4, 4, 7, 6, 7]
# nums = [6]
print(Solution().minSubsequence(nums))
