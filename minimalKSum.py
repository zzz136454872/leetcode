from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        tmp = nums
        tmp.sort()
        nums = []

        for i in range(len(tmp)):
            if i == 0 or tmp[i] != tmp[i - 1]:
                nums.append(tmp[i])

        n = len(nums)
        t = n + k
        s = (t + 1) * t // 2
        deleted = set()
        dc = 0

        for num in nums:
            if num <= t:
                s -= num
                deleted.add(num)
            else:
                dc += 1
        now = t

        for i in range(dc):
            while now in deleted:
                now -= 1
            s -= now
            now -= 1

        return s


nums = [1, 4, 25, 10, 25]
k = 2
nums = [5, 6]
k = 6
# nums=[96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
# k=35
print(Solution().minimalKSum(nums, k))
