from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0]

        for num in nums:
            preSum.append(preSum[-1] + num)
        print(preSum)

        q = deque()
        res = 1234567

        for i in range(len(preSum)):
            while len(q) > 0 and preSum[q[0]] + k <= preSum[i]:
                res = min(res, i - q[0])
                q.popleft()

            while len(q) > 0 and preSum[q[-1]] >= preSum[i]:
                q.pop()

            q.append(i)

        if res == 1234567:
            return -1

        return res


nums = [1]
k = 1
# nums = [1,2]
# k = 4
# nums = [2,-1,2]
# k = 3
print(Solution().shortestSubarray(nums, k))
