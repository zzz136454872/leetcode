from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        big = 10**7 + 7
        mem = [0, -big, -big]

        for num in nums:
            nmem = [0, 0, 0]
            t = num % 3
            nmem[t] = max(mem[t], mem[0] + num)
            nmem[(t + 1) % 3] = max(mem[(t + 1) % 3], mem[1] + num)
            nmem[(t + 2) % 3] = max(mem[(t + 2) % 3], mem[2] + num)
            mem = nmem

        return mem[0]


nums = [3, 6, 5, 1, 8]
nums = [4]
nums = [1, 2, 3, 4, 4]
print(Solution().maxSumDivThree(nums))
