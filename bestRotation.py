from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)

        for i in range(n):
            l1 = 0
            r1 = max(i - nums[i], -1)
            l2 = i + 1
            r2 = min((i + n - nums[i]), n - 1)
            diff[l1] += 1
            diff[l2] += 1
            diff[r1 + 1] -= 1
            diff[r2 + 1] -= 1

        maxLoc = 0
        m = 0
        now = 0

        for i in range(n):
            now += diff[i]

            if now > m:
                maxLoc = i
                m = now

        return maxLoc


nums = [2, 3, 1, 4, 0]
nums = [1, 3, 0, 2, 4]
print(Solution().bestRotation(nums))
