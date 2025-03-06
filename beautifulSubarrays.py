from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        tmp = 0
        res = 0
        mem[0] = 1

        for num in nums:
            tmp ^= num
            res += mem[tmp]
            mem[tmp] += 1

        return res


nums = [4, 3, 1, 2, 4]
nums = [1, 10, 4]

print(Solution().beautifulSubarrays(nums))
