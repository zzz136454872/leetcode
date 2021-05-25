from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxium = 8
        table = [123456789 for i in range(maxium)]
        table[0] = 0
        ncount = [{} for i in range(k)]

        for i in range(n):
            ncount[i % k][nums[i]] = ncount[i % k].get(nums[i], 0) + 1
        # print(ncount)

        tcount = [sum(ncount[i].values()) for i in range(k)]
        # print(tcount)

        for i in range(k):
            table_old = table
            table = [0 for i in range(maxium)]
            # print(i,table_old)
            tmp1 = min(table_old)

            for target in range(maxium):
                tmp2 = 1234567899

                for num in ncount[i]:
                    tmp2 = min(tmp2, table_old[target ^ num] - ncount[i][num])
                # print('tmp1',tmp1,'tmp2',tmp2)
                table[target] = min(tmp1, tmp2) + tcount[i]
            # print(table)

        return table[0]


sl = Solution()
nums = [3, 4, 5, 2, 1, 7, 3, 4, 7]
k = 3
print(sl.minChanges(nums, k))
