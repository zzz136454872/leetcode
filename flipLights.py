from typing import List


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 6)
        p = min(presses, 8)
        state = [0] * n
        res = set()

        for i in range(p + 1):
            for j in range(p - i + 1):
                for k in range(p - i - j + 1):
                    ll = p - i - j - k
                    # print(i,j,k,ll)
                    state = [1] * n

                    if i % 2 == 1:
                        state = [-1] * n

                    if j % 2 == 1:
                        state = [
                            -state[m] if m % 2 == 0 else state[m]
                            for m in range(len(state))
                        ]

                    if k % 2 == 1:
                        state = [
                            -state[m] if m % 2 != 0 else state[m]
                            for m in range(len(state))
                        ]

                    if ll % 2 == 1:
                        state = [
                            -state[m] if m % 3 == 0 else state[m]
                            for m in range(len(state))
                        ]
                    # print(state)
                    res.add(tuple(state))

        return len(res)


n = 6
presses = 1
print(Solution().flipLights(n, presses))
