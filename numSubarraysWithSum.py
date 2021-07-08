from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        now = 0
        mem = []

        for num in nums:
            if num == 0:
                now += 1
            else:
                mem.append(now)
                now = 0
        mem.append(now)
        out = 0

        if goal == 0:
            for num in mem:
                out += (num + 1) * num // 2

            return out

        for i in range(len(mem) - goal):
            out += (mem[i] + 1) * (mem[i + goal] + 1)

        return out


sl = Solution()
nums = [1, 0, 1, 0, 1]
goal = 2
nums = [0, 0, 0, 0, 0]
goal = 0
print(sl.numSubarraysWithSum(nums, goal))
