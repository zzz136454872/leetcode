from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        d = 1234567
        nums.sort()

        for i in range(len(nums) - 2):
            k = len(nums) - 1

            for j in range(i + 1, len(nums) - 1):
                t = nums[i] + nums[j] + nums[k]
                nd = abs(t - target)

                while t >= target:
                    if nd < d:
                        print(i, j, k, t, nd, d)
                        d = nd
                        res = t
                    k -= 1

                    if k <= j:
                        break
                    t = nums[i] + nums[j] + nums[k]
                    nd = abs(t - target)

                if nd < d:
                    # print(i,j,k,t,nd,d)
                    d = nd
                    res = t

                if k <= j:
                    break

        return res


nums = [-1, 2, 1, -4]
target = 1
nums = [0, 0, 0]
target = 1
print(Solution().threeSumClosest(nums, target))
