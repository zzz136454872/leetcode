from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        dp = 0
        presum = 0
        mod = 10**9 + 7

        for num in nums:
            dp = (num + presum) % mod
            presum = (presum + dp) % mod
            res = (res + dp * num**2) % mod

        return res


nums = [2, 1, 4]
print(Solution().sumOfPower(nums))
