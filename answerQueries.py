from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presum = [0]
        t = 0

        for num in nums:
            t += num
            presum.append(t)
        res = []

        for q in queries:
            l = 0
            r = len(presum) - 1

            while l <= r:
                m = (l + r) // 2

                if presum[m] <= q:
                    l = m + 1
                else:
                    r = m - 1
            res.append(r)

        return res


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
nums = [2, 3, 4, 5]
queries = [1]
print(Solution().answerQueries(nums, queries))
