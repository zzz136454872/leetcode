from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        s = sum(nums) / 2
        heapify(nums)
        res = 0

        while True:
            tmp = heappop(nums) / 2
            s -= tmp
            res += 1

            if s >= 0:
                return res
            heappush(nums, tmp)

        return -1


nums = [5, 19, 8, 1]
nums = [3, 8, 20]
print(Solution().halveArray(nums))
