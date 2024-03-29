from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mem = {}

        for num in arr:
            mem[num] = mem.get(num - difference, 0) + 1

        return max(mem.values())


arr = [1, 2, 3, 4]
difference = 1
arr = [1, 3, 5, 7]
difference = 1
arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
difference = -2
print(Solution().longestSubsequence(arr, difference))
