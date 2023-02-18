from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = 0
        res = 0
        mem = [0]

        for i in range(len(hours)):
            if hours[i] > 8:
                n += 1
            else:
                n -= 1
            mem.append(n)

        mem1 = [(0, 0)]

        for i in range(len(mem)):
            if mem[i] < mem1[0][0]:
                mem1.insert(0, (mem[i], i))
            elif mem[i] == mem1[0][0]:
                continue
            l = 0
            r = len(mem1) - 1

            while l <= r:
                mid = (l + r) // 2

                if mem1[mid][0] < mem[i]:
                    l = mid + 1
                else:
                    r = mid - 1

            if r >= 0:
                res = max(res, i - mem1[r][1])

        return res


#   0  9 9 6 0  6
# 0 -1 0 1 0 -1 -2
hours = [1, 9, 9, 6, 0, 6, 6, 9]
hours = [6, 6, 6]
# hours=[6,9,9]
# hours=[9,9,9]
print(Solution().longestWPI(hours))
