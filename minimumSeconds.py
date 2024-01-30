from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        mem = {}

        for i, v in enumerate(nums):
            if v not in mem:
                mem[v] = [i]
            else:
                mem[v].append(i)
        res = len(nums)

        for v in mem.values():
            diff = 0

            for i in range(len(v) - 1):
                diff = max(diff, v[i + 1] - v[i])
            diff = max(diff, v[0] + len(nums) - v[-1])
            res = min(res, diff // 2)

        return res


nums = [1, 2, 1, 2]
# nums=[2,1,3,3,2]
nums = [5, 5, 5, 5]
print(Solution().minimumSeconds(nums))
