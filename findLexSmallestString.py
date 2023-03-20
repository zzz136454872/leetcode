from typing import List


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        mem = set()
        s = list(map(int, list(s)))
        n = len(s)

        def gen(s):
            t1 = s[-b:] + s[:-b]
            tt1 = tuple(t1)

            if tt1 not in mem:
                mem.add(tt1)
                gen(t1)

            for i in range(1, n, 2):
                s[i] = (s[i] + a) % 10
            ts = tuple(s)

            if ts not in mem:
                mem.add(ts)
                gen(s)

        gen(s)
        # print(mem)

        return ''.join(map(str, sorted(mem)[0]))


s = "5525"
a = 9
b = 2
s = "74"
a = 5
b = 1
s = "0011"
a = 4
b = 2
s = "43987654"
a = 7
b = 3
print(Solution().findLexSmallestString(s, a, b))
