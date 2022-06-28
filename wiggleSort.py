from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        base = len(nums) // 2

        if len(nums) % 2 != 0:
            base += 1
        res1 = []
        res2 = []

        for i in range(len(nums) // 2):
            res1.append(nums[i])
            res1.append(nums[i + base])
            res2.append(nums[i + base])
            res2.append(nums[i])

        res2 = res2[::-1]

        if len(nums) % 2 != 0:
            res1.append(nums[len(nums) // 2])

        res = res1

        for i in range(len(res) - 1):
            if res[i] == res[i + 1]:
                res = res2

                break

        for i in range(len(res)):
            nums[i] = res[i]


nums = [1, 5, 1, 1, 6, 4]
nums = [1, 3, 2, 2, 3, 1]
nums = [1, 1, 2]
nums = [1, 1, 2, 1, 2, 2, 1]
nums = [4, 5, 5, 6]
Solution().wiggleSort(nums)
print(nums)
