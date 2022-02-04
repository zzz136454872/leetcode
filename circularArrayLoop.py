from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def jump(i):
            return (i + nums[i]) % n

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            p = i
            q = jump(i)
            direction = nums[i]

            while p != q:
                if direction * nums[p] <= 0:
                    break

                if direction * nums[q] <= 0:
                    break
                q = jump(q)

                if p == q:
                    break

                if direction * nums[q] <= 0:
                    break
                p = jump(p)
                q = jump(q)

                if p == q:
                    break

            if p == q:
                if p == jump(p):
                    continue

                return True
            q = i

            while q != p:
                tmp = jump(q)
                nums[q] = 0
                q = tmp

        return False


nums = [2, -1, 1, 2, 2]
# nums = [-1,2]
# nums = [-2,1,-1,-2,-2]
# nums=[-1,-2,-3,-4,-5]
nums = [3, 1, 2]
print(Solution().circularArrayLoop(nums))
