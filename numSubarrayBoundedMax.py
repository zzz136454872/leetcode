from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int,
                              right: int) -> int:
        last1 = -1
        last2 = -1

        res = 0

        for i in range(len(nums)):
            if left <= nums[i] and nums[i] <= right:
                last1 = i
            elif nums[i] > right:
                last2 = i
                last1 = -1

            if last1 != -1:
                res += last1 - last2

            print(i, last1, last2, res)

        return res


nums = [2, 1, 4, 3]
# nums=[2,2,2]
left = 2
right = 3

# nums = [2,9,2,5,6]
# left = 2
# right = 8

nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
left = 32
right = 69
print(Solution().numSubarrayBoundedMax(nums, left, right))
