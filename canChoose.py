from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0

        for g in groups:
            find = False

            while not find:
                find = True

                for j in range(len(g)):
                    if i + j >= len(nums):
                        return False

                    if nums[i + j] != g[j]:
                        find = False

                        break

                if find:
                    i += len(g)
                else:
                    i += 1

        return True


groups = [[1, -1, -1], [3, -2, 0]]
nums = [1, -1, 0, 1, -1, -1, 3, -2, 0]
groups = [[10, -2], [1, 2, 3, 4]]
nums = [1, 2, 3, 4, 10, -2]
groups = [[1, 2, 3], [3, 4]]
nums = [7, 7, 1, 2, 3, 4, 7, 7]
print(Solution().canChoose(groups, nums))
