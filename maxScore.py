from typing import *


# 不知道是哪个
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        log1 = [0 for i in range(n + 1)]
        log2 = [0 for i in range(n + 1)]
        tmp = 0

        for i in range(n):
            tmp += cardPoints[i]
            log1[i + 1] = tmp
        tmp = 0

        for i in range(n - 1, -1, -1):
            tmp += cardPoints[i]
            log2[i] = tmp
        out = 0
        # print(log1)
        # print(log2)

        for i in range(k + 1):
            out = max(out, log1[i] + log2[n - k + i])
            # print(i,out)

        return out


# N 次操作后的最大分数和
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        g = {n1: {n2: gcd(n1, n2) for n2 in nums} for n1 in nums}

        def calc(level, nums):
            if len(nums) == 0:
                return 0
            max_num = 0

            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    new_num = nums.copy()
                    del new_num[j]
                    del new_num[i]
                    now = g[nums[i]][nums[j]] * level + calc(
                        level + 1, new_num)
                    max_num = max(max_num, now)

            return max_num

        return calc(1, nums)


#  分割字符串的最大得分
class Solution:
    def maxScore(self, s: str) -> int:
        now = s[1:].count('1')

        if s[0] == '0':
            now += 1
        out = now

        for letter in s[1:len(s) - 1]:
            if letter == '0':
                now += 1
            else:
                now -= 1
            out = max(now, out)

        return out


sl = Solution()
nums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
s = "011101"
s = "00111"
# s = "111"
print(sl.maxScore(s))
