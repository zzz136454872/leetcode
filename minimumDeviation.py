from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minium = -1234567890

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] *= 2
            nums[i] = -nums[i]
            minium = max(minium, nums[i])

        heapify(nums)
        heap = nums
        out = minium - heap[0]

        while heap[0] % 2 == 0:
            now = heappop(heap)
            now //= 2
            minium = max(minium, now)
            heappush(heap, now)
            out = min(out, minium - heap[0])

        return out


# nums = [1, 2, 3, 4]
nums = [4, 1, 5, 20, 3]
# nums = [2,10,8]
print(Solution().minimumDeviation(nums))
