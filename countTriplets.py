from collections import Counter
from typing import List


# 不知道是哪个
class Solution1:
    def countTriplets(self, arr: List[int]) -> int:
        out = 0
        n = len(arr)

        for i in range(n - 1):
            tmp = arr[i]

            for j in range(i + 1, n):
                tmp ^= arr[j]

                if tmp == 0:
                    out += j - i

        return out


# sl=Solution()
# arr = [7,11,12,9,5,2,7,17,22]
# print(sl.countTriplets(arr))


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        mem = Counter([x & y for x in nums for y in nums])
        res = 0

        for k in mem:
            t = mem[k]

            for x in nums:
                if x & k == 0:
                    res += t

        return res


nums = [2, 1, 3]

print(Solution().countTriplets(nums))
