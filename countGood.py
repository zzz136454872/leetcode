from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        t = 0
        mem = defaultdict(int)
        res = 0
        j = 0

        for num in nums:
            t += mem[num]
            mem[num] += 1

            while t >= k:
                mem[nums[j]] -= 1
                t -= mem[nums[j]]
                j += 1
            res += j
            # print(num,t,k,j)

        return res


nums = [1, 1, 1, 1, 1]
k = 10
nums = [3, 1, 4, 3, 2, 2, 4]
k = 2
print(Solution().countGood(nums, k))
