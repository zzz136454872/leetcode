from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        p = [0]

        for i in range(len(nums)):
            p.append(p[-1] + nums[i])

        m1 = []

        for i in range(len(p) - firstLen):
            m1.append(p[i + firstLen] - p[i])

        m2 = []

        for i in range(len(p) - secondLen):
            m2.append(p[i + secondLen] - p[i])

        res = 0

        for i in range(len(nums) - firstLen + 1):
            for j in range(i - secondLen + 1):
                # print(i,j,firstLen,secondLen,len(nums),'flag')
                res = max(res, m1[i] + m2[j])

            for j in range(i + firstLen, len(m2)):
                # print(i,j,firstLen,secondLen,len(nums))
                res = max(res, m1[i] + m2[j])

        return res


nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
firstLen = 1
secondLen = 2
nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
firstLen = 3
secondLen = 2
nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
firstLen = 4
secondLen = 3

nums = [12, 8, 12, 18, 19, 10, 17, 20, 6, 8, 13, 1, 19, 11, 5]
firstLen = 3
secondLen = 6
print(Solution().maxSumTwoNoOverlap(nums, firstLen, secondLen))
