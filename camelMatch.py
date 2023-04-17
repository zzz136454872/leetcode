from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def t(a):
            if a.isupper():
                return 1

            return 0

        def cut(s):
            res = []

            if s[0].isupper():
                res.append('')

            for letter in s:
                if letter.isupper():
                    res.append(letter)
                    res.append('')
                else:
                    if len(res) > 0 and (len(res[-1]) == 0
                                         or res[-1].islower()):
                        res[-1] += letter
                    else:
                        res.append(letter)

            return res

        def matchSub(a, b):
            if a == b:
                return True

            if a.isupper() or b.isupper():
                return False
            i = 0
            j = 0

            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            return j == len(b)

        def match(a, b):
            if len(a) != len(b):
                return False

            for i in range(len(a)):
                if not matchSub(a[i], b[i]):
                    return False

            return True

        p = cut(pattern)
        # print([cut(q) for q in queries])

        return [match(cut(q), p) for q in queries]


queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FB"
queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBa"
queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBaT"

queries = [
    "uAxaqlzahfialcezsLfj", "cAqlzyahaslccezssLfj", "AqlezahjarflcezshLfj",
    "AqlzofahaplcejuzsLfj", "tAqlzahavslcezsLwzfj", "AqlzahalcerrzsLpfonj",
    "AqlzahalceaczdsosLfj", "eAqlzbxahalcezelsLfj"
]
pattern = "AqlzahalcezsLfj"
print(Solution().camelMatch(queries, pattern))
