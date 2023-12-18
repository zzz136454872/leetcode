from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        fn = 0
        fp = 0
        res = 0

        for i, num in enumerate(nums):
            if num > 0:
                fp += 1

                if fn > 0:
                    fn += 1
            elif num < 0:
                if fn > 0:
                    fp, fn = fn + 1, fp + 1
                else:
                    fp, fn = 0, fp + 1
            else:
                fp = 0
                fn = 0
            res = max(res, fp)

        return res


nums = [1, -2, -3, 4]
# nums = [0,1,-2,-3,-4]
# nums = [-1,-2,-3,0,1]
nums = [1, 2, 3, 5, -6, 4, 0, 10]
print(Solution().getMaxLen(nums))
