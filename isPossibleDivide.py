from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if k == 1:
            return True

        if len(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        n = len(nums) // k

        for i in range(n):
            a = nums.pop() + 1

            for j in range(k - 1):
                find = False
                left = 0
                right = len(nums) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if nums[mid] > a:
                        left = mid + 1
                    elif nums[mid] < a:
                        right = mid - 1
                    else:
                        find = True
                        del nums[mid]
                        a += 1

                        break

                if not find:
                    return False
            # print(nums)

        return True


nums = [1, 2, 3, 6, 2, 3, 4, 7, 8]
k = 3
nums = [1, 2, 3, 3, 4, 4, 5, 6]
k = 4
nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3
nums = [16, 21, 26, 35]
k = 4
print(Solution().isPossibleDivide(nums, k))
