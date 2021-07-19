from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        s = 0
        h = 0
        out = 1

        for i in range(len(nums)):
            s += (i - j) * (nums[i] - h)

            while s > k:
                s -= (nums[i] - nums[j])
                j += 1
            # print(s,i,j)
            out = max(out, i - j + 1)
            h = nums[i]

        return out


sl = Solution()
nums = [1, 2, 4]
k = 5
nums = [1, 4, 8, 13]
k = 5
nums = [3, 9, 6]
k = 2
print(sl.maxFrequency(nums, k))
