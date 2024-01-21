from functools import cache
from typing import List


# 不知道是哪个
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start = max(nums)
        end = sum(nums)

        while start < end:
            mid = (start + end) // 2
            count = 1
            s = 0

            for num in nums:
                s += num

                if s > mid:
                    count += 1
                    s = num

            if count > m:
                start = mid + 1
            else:
                end = mid

        return start


# 410. 分割数组的最大值
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        right = sum(nums)
        left = max(nums)

        while left <= right:
            mid = (left + right) // 2
            c = 1
            t = 0

            for num in nums:
                t += num

                if t > mid:
                    c += 1
                    t = num

            if c > k:
                left = mid + 1
            else:
                right = mid - 1

        return left


nums = [7, 2, 5, 10, 8]
k = 2
nums = [1, 2, 3, 4, 5]
k = 2
# nums = [1, 4, 4]
# k = 3
print(Solution().splitArray(nums, k))
