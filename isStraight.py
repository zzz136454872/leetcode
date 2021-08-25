from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0

        while nums[i] == 0:
            i += 1
        nums = nums[i:]
        j = 1

        for num in nums:
            if nums.count(num) > 1:
                return False

        while j < len(nums):
            i -= (nums[j] - nums[j - 1] - 1)
            j += 1

        return i >= 0


sl = Solution()
nums = [0, 0, 1, 2, 6]
print(sl.isStraight(nums))
