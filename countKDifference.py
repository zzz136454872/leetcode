from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mem = {}
        out = 0

        for num in nums:
            out += mem.get(num + k, 0)
            out += mem.get(num - k, 0)
            mem[num] = mem.get(num, 0) + 1

        return out


nums = [1, 2, 2, 1]
k = 1
print(Solution().countKDifference(nums, k))
