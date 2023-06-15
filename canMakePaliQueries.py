from typing import List


class Solution:
    def canMakePaliQueries(self, s: str,
                           queries: List[List[int]]) -> List[bool]:
        mem = [0] * 26

        def l2n(a):
            return ord(a) - ord('a')

        presum = [mem.copy()]

        for letter in s:
            mem[l2n(letter)] += 1
            presum.append(mem.copy())

        res = []

        for q in queries:
            diff = sum([(presum[q[1] + 1][i] - presum[q[0]][i]) % 2
                        for i in range(26)])
            # print(q, diff)

            if diff <= 2 * q[2] or diff == 2 * q[2] + 1 and (q[1] -
                                                             q[0]) % 2 == 0:
                res.append(True)
            else:
                res.append(False)

        return res


s = "abcda"
queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]

print(Solution().canMakePaliQueries(s, queries))
