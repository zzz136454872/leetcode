from typing import *


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 4 != 0:
            return False
        target //= 4

        for num in nums:
            if num > target:
                return False

        nums.sort(reverse=True)
        edge = [0] * 4

        def dfs(idx):
            if idx == len(nums):
                return True

            for i in range(4):
                if edge[i] + nums[idx] <= target:
                    edge[i] += nums[idx]

                    if dfs(idx + 1):
                        return True
                    edge[i] -= nums[idx]

            return False

        return True


sl = Solution()
inp = [1, 1, 2, 2, 2]
print(sl.makesquare(inp))
