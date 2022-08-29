from random import randint
from typing import List


# 不知道是哪个
class Solution1:
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


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])

        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(Solution().shuffle(nums, n))
