from typing import List


# 不知道是哪个
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(nums[i], i) for i in range(len(nums))])
        i = 0
        j = len(nums) - 1

        while i < j:
            a = nums[i][0] + nums[j][0]

            if a == target:
                return [nums[i][1], nums[j][1]]
            elif a > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]


# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6
# nums = [3, 2, 4]
# target = 6
# print(Solution().twoSum(nums, target))


# 167. 两数之和 II - 输入有序数组
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted([(numbers[i], i) for i in range(len(numbers))])
        i = 0
        j = len(numbers) - 1

        while i < j:
            a = numbers[i][0] + numbers[j][0]

            if a == target:
                return [i + 1, j + 1]
            elif a > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9
numbers = [2, 3, 4]
target = 6
print(Solution().twoSum(numbers, target))
