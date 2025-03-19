from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mem = []

        for num in nums:
            inserted = False

            for m in mem:
                if num not in m:
                    inserted = True
                    m.add(num)

                    break

            if not inserted:
                mem.append(set([num]))

        return [list(m) for m in mem]


nums = [1, 3, 4, 1, 2, 3, 1]
nums = [1, 2, 3, 4]
print(Solution().findMatrix(nums))
