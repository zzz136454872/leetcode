from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def bigger(a, b):
            if a == '-1':
                return False

            if b == '-1':
                return True

            if len(a) != len(b):
                return len(a) > len(b)

            for i in range(len(a)):
                if ord(a[i]) != ord(b[i]):
                    return ord(a[i]) > ord(b[i])

            return False

        mem = [-1] * (target + 1)
        mem[0] = 0
        log = ['-1'] * (target + 1)
        log[0] = ''

        for i in range(1, target + 1):
            # print(i,log)

            for j in range(9):
                if cost[j] <= i and log[i - cost[j]] != '-1':
                    tmp = str(j + 1) + log[i - cost[j]]
                    # print(tmp,i,log[i],bigger(tmp,log[i]))

                    if bigger(tmp, log[i]):
                        log[i] = tmp

        if log[-1] == '-1':
            return '0'

        return log[-1]


sl = Solution()
cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
target = 9
cost = [7, 6, 5, 5, 5, 6, 8, 7, 8]
target = 12
cost = [6, 10, 15, 40, 40, 40, 40, 40, 40]
target = 47
cost = [2, 4, 6, 2, 4, 6, 4, 4, 4]
target = 5
print(sl.largestNumber(cost, target))
