from heapq import heappop, heappush
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        heap = []
        blood = 1
        move = 0

        for num in nums:
            if num < 0:
                heappush(heap, num)

                if blood + num <= 0:
                    tmp = heappop(heap)
                    move += 1
                    blood -= tmp
            blood += num

        return move


sl = Solution()
nums = [100, 100, 100, -250, -60, -140, -50, -50, 100, 150]
nums = [-200, -300, 400, 0]
print(sl.magicTower(nums))
