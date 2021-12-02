from typing import *


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        out = 0

        for num in nums:
            out = out ^ num

        return out


#I. 数组中数字出现的次数

from functools import reduce


class Solution1:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ab = reduce(lambda a, b: a ^ b, nums)
        last = ab & (-ab)
        a = 0

        for num in nums:
            if num & last:
                a ^= num

        return [a, ab ^ a]


# sl = Solution()
# nums = [4, 1, 4, 6]
# print(sl.singleNumbers(nums))


# II. 数组中数字出现的次数 II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0

        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one

        return one


nums = [3, 4, 3, 3]
nums = [9, 1, 7, 9, 7, 9, 7]
print(Solution().singleNumber(nums))
