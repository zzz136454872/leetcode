from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        table = {0: 1}

        for num in nums:
            table_old = table
            table = {}

            for k in table_old:
                tmp = table.get(k + num, 0) + table_old.get(k, 0)

                if tmp:
                    table[k + num] = tmp
                tmp2 = table.get(k - num, 0) + table_old.get(k, 0)

                if tmp2:
                    table[k - num] = tmp2
            # print(num, table)

        return table.get(target, 0)


sl = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
nums = [1]
target = 1
nums = [1, 0]
target = 1
print(sl.findTargetSumWays(nums, target))
