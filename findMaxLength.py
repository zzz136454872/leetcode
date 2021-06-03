from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tmp = 0
        n = len(nums)
        log = [0] * (n + 1)
        tmp = 0

        for i in range(n):
            tmp += 1 if nums[i] == 0 else -1
            log[i + 1] = tmp
        counter = {}
        out = 0

        for i in range(n + 1):
            if log[i] in counter:
                out = max(out, i - counter[log[i]])
            else:
                counter[log[i]] = i

        return out


sl = Solution()
nums = [0, 1, 0]
print(sl.findMaxLength(nums))
