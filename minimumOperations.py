from typing import List


# 不知道是哪个
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set(nums)
        a.discard(0)

        return len(a)


# 3396. 使数组元素互不相同所需的最少操作次数
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mem = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in mem:
                return i // 3 + 1
            mem.add(nums[i])

        return 0


nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
nums = [1, 2, 3, 4, 4]
print(Solution().minimumOperations(nums))
