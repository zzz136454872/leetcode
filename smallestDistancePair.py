from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]

        def count(k):
            r = 0
            res = 0

            for l in range(n - 1):
                while r < n and nums[r] - nums[l] <= k:
                    r += 1
                res += r - l - 1

            return res

        while left <= right:
            mid = (left + right) // 2

            if count(mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left


nums = [1, 3, 1]
k = 1
nums = [1, 3, 1]
k = 1
nums = [1, 6, 1]
k = 3
print(Solution().smallestDistancePair(nums, k))
