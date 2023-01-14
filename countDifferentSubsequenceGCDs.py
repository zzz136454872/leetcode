from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        m = max(nums) + 1
        mem = [False for i in range(m)]

        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        for num in nums:
            mem[num] = True

        res = 0

        for i in range(1, m):
            subGcd = 0

            for j in range(i, m, i):
                if mem[j]:
                    if subGcd == 0:
                        subGcd = j
                    else:
                        subGcd = gcd(subGcd, j)

                    if subGcd == i:
                        res += 1

                        break

        return res


nums = [6, 10, 3]
print(Solution().countDifferentSubsequenceGCDs(nums))
