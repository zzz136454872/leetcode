from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bitLen = 31
        c0 = [0 for i in range(bitLen)]
        out = 0

        for i in range(len(nums)):
            n = bin(nums[i])[2:]
            n = '0' * (bitLen - len(n)) + n

            for j in range(bitLen):
                if n[j] == '0':
                    out += (i - c0[j])
                    c0[j] += 1
                else:
                    out += c0[j]

        return out


sl = Solution()
nums = [4, 14, 2]
print(sl.totalHammingDistance(nums))
