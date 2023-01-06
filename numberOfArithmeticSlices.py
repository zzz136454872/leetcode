from collections import defaultdict
from typing import List


# 等差数列划分
class Solution1:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        out = 0
        val = -1
        count = 0

        for v in diff:
            if v == val:
                count += 1
                out += count - 1
            else:
                count = 1
                val = v

        return out


def comb(a, b):
    out = 1

    for i in range(b):
        out = out * (a - i) // (i + 1)

    return out


# sl = Solution()
# nums = [1, 2, 3, 4]
# nums = [1]
# print(sl.numberOfArithmeticSlices(nums))


#  等差数列划分 II - 子序列
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        mem = defaultdict(lambda: defaultdict(int))
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = mem[j][d]
                res += cnt
                mem[i][d] += cnt + 1

        return res


# nums = [2,4,6,8,10]
nums = [7, 7, 7, 7, 7]

sl = Solution()
print(sl.numberOfArithmeticSlices(nums))
