from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n1 = []
        n2 = []
        n3 = []

        for num in nums:
            if num < pivot:
                n1.append(num)
            elif num == pivot:
                n2.append(num)
            else:
                n3.append(num)

        return n1 + n2 + n3


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
nums = [-3, 4, 3, 2]
pivot = 2
print(Solution().pivotArray(nums, pivot))
