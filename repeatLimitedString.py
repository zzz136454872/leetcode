from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a = Counter(s)
        res = []
        a = sorted(a.items(), key=lambda x: ord(x[0]))
        a = [list(aa) for aa in a]

        while len(a) > 0:
            if a[-1][1] > repeatLimit:
                a[-1][1] -= repeatLimit
                res.append(a[-1][0] * repeatLimit)

                if len(a) > 1:
                    res.append(a[-2][0])
                    a[-2][1] -= 1

                    if a[-2][1] == 0:
                        del a[-2]
                else:
                    break
            else:
                res.append(a[-1][0] * a[-1][1])
                a.pop()

        return ''.join(res)


s = "cczazcc"
repeatLimit = 3
s = "aababab"
repeatLimit = 2
print(Solution().repeatLimitedString(s, repeatLimit))
