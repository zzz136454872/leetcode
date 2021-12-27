from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        i = 0

        while i < len(ages) and ages[i] <= 14:
            i += 1

        if i == len(ages):
            return 0
        prev = ages[i]
        mem = [[prev, 1]]
        i += 1

        while i < len(ages):
            if ages[i] == prev:
                mem[-1][1] += 1
            else:
                mem.append([ages[i], 1])
                prev = ages[i]
            i += 1
        preSum = [0 for i in range(len(mem) + 1)]
        tmp = 0

        for i in range(len(mem)):
            tmp += mem[i][1]
            preSum[i + 1] = tmp

        out = 0
        j = 0

        for i in range(len(mem)):
            out += mem[i][1] * (mem[i][1] - 1)
            test = 0.5 * mem[i][0] + 7

            while mem[j][0] <= test:
                j += 1
            out += (preSum[i] - preSum[j]) * mem[i][1]

        return out


ages = [16, 16]
ages = [16, 17, 18]
ages = [118, 14, 7, 63, 103]
# ages = [20,30,100,110,120]
# ages = [108,115,5,24,82]
# ages = [8,85,24,85,69]
print(Solution().numFriendRequests(ages))
