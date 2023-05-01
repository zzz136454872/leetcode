from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        mem = {}

        for num in nums:
            if num not in mem:
                mem[num] = {}

            for delta in range(-500, 501):
                if delta == 0:
                    mem[num][0] = mem[num].get(0, 0) + 1
                elif num - delta in mem:
                    mem[num][delta] = mem[num - delta].get(delta, 1) + 1
        res = 2

        for v in mem.values():
            if len(v) > 0:
                res = max(res, max(v.values()))

        return res


nums = [3, 6, 9, 12]
nums = [9, 4, 7, 2, 10]
nums = [20, 1, 15, 3, 10, 5, 8]
nums = [24, 13, 1, 100, 0, 94, 3, 0, 3]
print(Solution().longestArithSeqLength(nums))
