from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mem = {}

        for num in nums:
            mem[num] = mem.get(num, 0) + 1
        out = []

        for item in sorted(list(mem.items()), key=lambda x: (x[1], -x[0])):
            out += [item[0]] * item[1]

        return out


nums = [1, 1, 2, 2, 2, 3]
nums = [2, 3, 1, 3, 2]
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(Solution().frequencySort(nums))
