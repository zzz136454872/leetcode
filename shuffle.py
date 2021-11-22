from random import randint
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.ori = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        return self.ori

    def shuffle(self) -> List[int]:
        for j in range(len(self.ori) - 1, -1, -1):
            idx = randint(0, j)
            self.nums[idx], self.nums[j] = self.nums[j], self.nums[idx]

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
