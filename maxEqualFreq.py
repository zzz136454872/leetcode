from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        mem = {}
        mem2 = {}
        maxLen = 1
        maxCount = 0

        for i in range(len(nums)):
            num = nums[i]
            mem2[num] = mem2.get(num, 0) + 1
            k = mem2[num]

            if k not in mem:
                mem[k] = set([num])
                maxCount = max(k, maxCount)
            else:
                mem[k].add(num)

            if k != 1:
                mem[k - 1].remove(num)

            if maxCount == 1:
                maxLen = i + 1

                continue

            if len(mem[maxCount]) == 1 and maxCount + (maxCount - 1) * len(
                    mem[maxCount - 1]) == i + 1:
                maxLen = i + 1

                continue

            if len(mem[1]) == 1 and len(mem[maxCount]) * maxCount == i:
                maxLen = i + 1

        return maxLen


nums = [2, 2, 1, 1, 5, 3, 3, 5]
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
print(Solution().maxEqualFreq(nums))
