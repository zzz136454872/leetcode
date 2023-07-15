from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = target - nums[i] - nums[j]
                h = n - 1

                for k in range(j + 1, n - 1):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    while k < h and nums[k] + nums[h] > t:
                        h -= 1

                    if k >= h:
                        break

                    if nums[k] + nums[h] == t:
                        res.append([nums[i], nums[j], nums[k], nums[h]])

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [2, 2, 2, 2, 2]
target = 8
print(Solution().fourSum(nums, target))
