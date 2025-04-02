from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] < nums[j]:
                    continue

                for k in range(j + 1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])

        return res


nums = [12, 6, 1, 2, 7]
print(Solution().maximumTripletValue(nums))
