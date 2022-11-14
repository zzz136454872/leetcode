from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        nums = [x * n - s for x in nums]

        if len(nums) < 2:
            return False

        m = (n + 1) // 2
        l = nums[:m]
        r = nums[m:]

        def get(mask, arr):
            res = 0

            for i in range(len(arr)):
                if mask & (1 << i):
                    res += arr[i]

            return res

        ls = set()

        for i in range(1, 2**m):
            ls.add(get(i, l))

        if 0 in ls:
            return True

        for i in range(1, 2**len(r)):
            tmp = get(i, r)

            if tmp == 0 or (-tmp in ls and (tmp != sum(r) or -tmp != sum(l))):
                return True

        return False


nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = [3, 1]
nums = [0]

print(Solution().splitArraySameAverage(nums))
