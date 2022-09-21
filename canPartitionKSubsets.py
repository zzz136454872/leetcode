from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)

        if s % k != 0:
            return False
        p = s // k
        nums.sort()

        mem = {0: True}

        def sub(mask, now):
            if mask in mem:
                return mem[mask]

            for i in range(len(nums)):
                if mask & (1 << i) == 0:
                    continue

                if now + nums[i] > p:
                    break

                if sub(mask ^ (1 << i), (now + nums[i]) % p):
                    mem[mask] = True

                    return True
            mem[mask] = False

            return False

        return sub(2**len(nums) - 1, 0)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
# nums = [1,2,3,4]
# k = 3
print(Solution().canPartitionKSubsets(nums, k))
