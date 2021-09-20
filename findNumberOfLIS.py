from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        nums.append(1425678)
        n = len(nums)
        mem = [1] * n
        preMax = [1] * n
        counter = [1] * n

        for i in range(1, n):
            tmp = 1

            for j in range(i - 1, -1, -1):
                if preMax[j] + 1 < tmp:
                    break

                if nums[j] >= nums[i]:
                    continue

                if mem[j] + 1 > tmp:
                    tmp = mem[j] + 1
                    counter[i] = counter[j]
                elif mem[j] + 1 == tmp:
                    counter[i] += counter[j]
            mem[i] = tmp
            preMax[i] = max(tmp, preMax[i - 1])


        return counter[-1]


nums = [1, 3, 5, 4, 7]
print(Solution().findNumberOfLIS(nums))
