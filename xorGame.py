from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        x = 0
        for num in nums:
            x ^= num
        return x == 0


sl = Solution()
nums = [1, 1, 2]
print(sl.xorGame(nums))
