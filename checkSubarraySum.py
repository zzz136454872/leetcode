from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        preSum = [0] * (n + 1)

        tmp = 0

        for i in range(n):
            tmp = (tmp + nums[i]) % k
            preSum[i + 1] = tmp

        hashTable = {}

        for i, t in enumerate(preSum):
            if t in hashTable:
                if i - hashTable[t] > 1:
                    return True
            else:
                hashTable[t] = i

        return False


sl = Solution()
nums = [23, 2, 4, 6, 7]
nums = [23, 2, 6, 4, 7]
k = 6
k = 13

nums = [0]
k = 1
print(sl.checkSubarraySum(nums, k))
