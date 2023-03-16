from collections import defaultdict
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        presum = defaultdict(int)
        t = 0
        res = 0
        presum[0] = 1
        i = 0

        while True:
            if nums[i] > k:
                t += 1
            elif nums[i] < k:
                t -= 1

            if nums[i] == k:
                break
            i += 1
            presum[t] += 1

        while i < len(nums):
            if nums[i] > k:
                t += 1
            elif nums[i] < k:
                t -= 1
            res += presum[t]
            res += presum[t - 1]
            i += 1

        return res


nums = [3, 2, 1, 4, 5]
k = 4
nums = [2, 3, 1]
k = 3
print(Solution().countSubarrays(nums, k))
