from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[j] - nums[i] != diff:
                    continue

                for k in range(j + 1, n):
                    if diff == nums[k] - nums[j]:
                        res += 1

        return res


nums = [0, 1, 4, 6, 7, 10]
diff = 3
nums = [4, 5, 6, 7, 8, 9]
diff = 2
print(Solution().arithmeticTriplets(nums, diff))
