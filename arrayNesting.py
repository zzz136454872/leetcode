from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            cnt = 0
            tmp = i

            while nums[tmp] != -1:
                cnt += 1
                nums[tmp], tmp = -1, nums[tmp]
            res = max(res, cnt)

        return res


A = [5, 4, 0, 3, 1, 6, 2]
print(Solution().arrayNesting(A))
