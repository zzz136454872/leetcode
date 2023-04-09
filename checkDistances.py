from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        def l2n(a):
            return ord(a) - ord('a')

        mem = [-1] * 26

        for i in range(len(s)):
            t = l2n(s[i])

            if mem[t] == -1:
                mem[t] = i
            else:
                mem[t] = i - mem[t] - 1

        for i in range(26):
            if mem[i] != -1 and mem[i] != distance[i]:
                return False

        return True


s = "abaccb"
distance = [
    1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]
s = "aa"
distance = [
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0
]
print(Solution().checkDistances(s, distance))
