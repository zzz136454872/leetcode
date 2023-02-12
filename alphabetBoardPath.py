from typing import List


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        loc = (0, 0)
        res = []

        def l2l(a):
            n = ord(a) - ord('a')

            return (n // 5, n % 5)

        for letter in target:
            t = l2l(letter)
            print(loc, t, letter)

            if loc[0] == 5:
                if loc[0] <= t[0]:
                    res.append('D' * (t[0] - loc[0]))
                else:
                    res.append('U' * (loc[0] - t[0]))

                if loc[1] <= t[1]:
                    res.append('R' * (t[1] - loc[1]))
                else:
                    res.append('L' * (loc[1] - t[1]))
            else:
                if loc[1] <= t[1]:
                    res.append('R' * (t[1] - loc[1]))
                else:
                    res.append('L' * (loc[1] - t[1]))

                if loc[0] <= t[0]:
                    res.append('D' * (t[0] - loc[0]))
                else:
                    res.append('U' * (loc[0] - t[0]))
            loc = t
            res.append('!')

        return ''.join(res)


# target = "leet"
target = "code"
print(Solution().alphabetBoardPath(target))
